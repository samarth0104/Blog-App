from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str


app = FastAPI()

# Mount the templates folder as a static directory
app.mount("/static", StaticFiles(directory="templates"), name="static")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["blog_database"]
posts_collection = db["posts"]
post_id_counter = db["post_id_counter"]

# Initialize post ID counter if not already initialized
if post_id_counter.count_documents({}) == 0:
    post_id_counter.insert_one({"id": 1})


@app.get("/")
async def index():
    return FileResponse("templates/index.html")


@app.get("/posts/", response_model=list)
async def get_posts():
    posts = list(posts_collection.find({}, {"_id": 0}))
    # Convert ObjectId to string for each post
    for post in posts:
        post["id"] = str(post["id"])
    return posts


@app.post("/posts/", response_model=dict)
async def create_post(post: PostCreate):
    # Get the current post ID and increment it
    post_id = post_id_counter.find_one_and_update({}, {"$inc": {"id": 1}})["id"]
    post_dict = post.dict()
    post_dict["id"] = post_id
    result = posts_collection.insert_one(post_dict)
    # Convert ObjectId to string for the created post
    post_dict["_id"] = str(result.inserted_id)
    return {"message": "Post created successfully", "id": post_id, **post_dict}


@app.get("/posts/{post_id}", response_model=dict)
async def get_post(post_id: int):
    post = posts_collection.find_one({"id": post_id}, {"_id": 0})
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")


class PostUpdate(BaseModel):
    title: str
    content: str


@app.put("/posts/{post_id}", response_model=dict)
async def update_post(post_id: int, post_data: PostUpdate):
    updated_post = {"title": post_data.title, "content": post_data.content}
    result = posts_collection.update_one({"id": post_id}, {"$set": updated_post})
    if result.modified_count == 1:
        return {"message": "Post updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{post_id}", response_model=dict)
async def delete_post(post_id: int):
    # Check if the post exists before attempting to delete it
    post = posts_collection.find_one({"id": post_id})
    if post:
        result = posts_collection.delete_one({"id": post_id})
        if result.deleted_count == 1:
            return {"message": "Post deleted successfully"}
    # If the post doesn't exist or deletion was unsuccessful, raise an HTTPException
    raise HTTPException(status_code=404, detail="Post not found")
