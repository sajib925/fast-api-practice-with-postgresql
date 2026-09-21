from pydantic import BaseModel, Field
from typing import Optional

class TodoPydantic(BaseModel):
    title : str = Field(max_length=40)
    description : str = Field(max_length=200)
    priority : int = Field(ge=0, le=5)
    completed : bool
    
class TodoPydanticUpdate(BaseModel):
    title : Optional[str] = Field(default=None, max_length=40)
    description : Optional[str] = Field(default=None, max_length=200)
    priority : Optional[int] = Field(default=None, ge=0, le=5)
    completed : Optional[bool] = Field(default=None)


class UserPydantic(BaseModel):
    email: str
    username: str
    firstname: str
    lastname: str
    password: str
    phone_number: str

class UserPydanticUpdate(BaseModel):
    email: Optional[str] = Field(default=None)
    username: Optional[str] = Field(default=None)
    firstname: Optional[str] = Field(default=None)
    lastname: Optional[str] = Field(default=None)
    phone_number: Optional[str] = Field(default=None)

class UserPydanticPasswordUpdate(BaseModel):
    current_pasword: str 
    new_pasword: str