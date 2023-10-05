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
    return all_posts


@router.post("/create")
def create_post(post: Post):
    post = post.model_dump()
    post['postId'] = randrange(0, 1000000)
    all_posts.append(post)
    # todo get userId from session and set it in the newly created post
    return post


@router.get("/{id}")
def get_post(id: int):
    for post in all_posts:
        if (post["postId"] == id):
            return post
    return {"data": "Post does not exists"}


@router.put("/update/{id}")
def update_post(post: Post):
    print(post)
    for my_post in all_posts:
        if my_post['postId'] == post.model_dump()['postId']:
            all_posts.remove(my_post)
            all_posts.append(post.model_dump())
    return post.model_dump()


@router.delete("/delete/{id}")
def delete_post(id: int):
    for post in all_posts:
        if post['postId'] == id:
            all_posts.remove(post)
            return {"message": "deleted"}
    return {"message": "post does not exists"}
