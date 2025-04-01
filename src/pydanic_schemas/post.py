from pydantic import BaseModel, field_validator


class Post(BaseModel):
    author: str
    author_bio: str
    id: int
    price: int
    title: str

    @field_validator('id')
    def check_that_id_is_less_than_fifty(cls, v):
        if v > 50:
            raise ValueError('id bigger than 50')
        else:
            return v