from pydantic import BaseModel, Field 
from fastapi_users import schemas
import uuid 


class PostCreate(BaseModel):
    title: str = Field(description="The title of the post")
    content: str = Field(description="The content of the post")


class PostResponse(BaseModel):
    title: str = Field(description="The title of the post")
    content: str = Field(description="The content of the post")

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass 

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass