from pydantic import BaseModel


class User(BaseModel):
    userId: int
    password: str


class Post(BaseModel):
    postId: int = None
    title: str
    content: str
    creatorId: int = None

class PostCreate(BaseModel):
    title: str
    content: str