from pydantic import BaseModel, Field 


class PostCreate(BaseModel):
    title: str = Field(description="The title of the post")
    content: str = Field(description="The content of the post")


class PostResponse(BaseModel):
    title: str = Field(description="The title of the post")
    content: str = Field(description="The content of the post")
