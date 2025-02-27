from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    tasks: List[Task]
    class Config:
        orm_mode = True

class ShowTask(BaseModel):
    title: str
    description: str
    completed: bool
    creator: ShowUser
    class Config:
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
