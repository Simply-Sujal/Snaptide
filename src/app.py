from typing import Dict, List, Union
from fastapi import FastAPI, HTTPException

from src.schema import PostCreate, PostResponse

app = FastAPI(title="Snaptide API", description="API for Snaptide")

text_posts = {
    1: {
        "title": "Post 1",
        "content": "Description of Post 1",
    },
    2: {
        "title": "Post 2",
        "content": "Description of Post 2",
    },
    3: {
        "title": "Post 3",
        "content": "Description of Post 3",
    },
    4: {
        "title": "Post 4",
        "content": "Description of Post 4",
    },
    5: {
        "title": "Post 5",
        "content": "Description of Post 5",
    },
    6: {
        "title": "Post 6",
        "content": "Description of Post 6",
    },
    7: {
        "title": "Post 7",
        "content": "Description of Post 7",
    },
}

@app.get("/posts")
def get_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if not id in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {
        "title": post.title,
        "content": post.content 
    }
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
 
@app.get("/health-check")
def health_check():
    return {"message": "Health check successful"}