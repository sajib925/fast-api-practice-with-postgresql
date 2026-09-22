from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL="postgresql://postgres:postgres@localhost:5432/todos"
SQLALCHEMY_DATABASE_URL="postgresql://neondb_owner:npg_UQtx02NXySRm@ep-quiet-mountain-aw28uu4r-pooler.c-12.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()