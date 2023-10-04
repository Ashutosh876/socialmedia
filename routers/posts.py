from fastapi import APIRouter
from schemas import Post
from random import randrange
from inventory import all_posts

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/")
def get_posts():
    return {"data": all_posts}


@router.post("/create")
def create_post(post: Post):
    post = post.model_dump()
    post['postId'] = randrange(0, 1000000)
    all_posts.append(post)
    # todo get userId from session and set it in the newly created post
    return {"data": post}

