from pydantic import BaseModel, Field


class Post(BaseModel):
    author: str
    author_bio: str
    id: int = Field(le=50)
    price: int
    title: str