from test.test_main import client
from main import app
from fastapi import status
from router.auth import get_current_user
from database import SessionLocal
from models import Todo
import pytest

def override_get_current_user():
    return {
        'id': 1,
        'username': 'testuser'
    }



@pytest.fixture
def test_todo():
  db = SessionLocal()
  todo = Todo(
      title='testing',
      description='testing',
      priority=2,
      completed=True,
      owner_id=1,
  )
  db.add(todo)
  db.commit()
  db.refresh(todo)

  yield todo  

  db.delete(todo)
  db.commit()

app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_todos():
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK

def test_read_spacific_todo(test_todo):
    response = client.get(f"/todo/{test_todo.id}")
    assert response.status_code == status.HTTP_200_OK
def test_create_todo():

    request_data = {
        "title": "string",
        "description": "string",
        "priority": 5,
        "completed": True
    }
    response = client.post(f"/create", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {'message': 'todo created successfully'}
    
def test_update_todo(test_todo):

    request_data = {
        'title': 'Updated Title', 
        'priority': 1
    }

    response = client.put(f"/edit/{test_todo.id}", json=request_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'todos updated successfully'}

def test_delete_todo(test_todo):

    response = client.delete(f"/delete/{test_todo.id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'todos deleted successfully'}
