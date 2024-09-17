from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dynamodb_tables import get_table

blogs_table = get_table("Blogs")

router = APIRouter() # FastAPI router for blog-related endpoints

# Blog model for adding/updating blogs
class Blog(BaseModel):
  itemId: str
  title: str
  description: str
  date: str  # YYYY-MM-DD format
  content: str

@router.get("/api/blogs")
async def get_all_blogs():
  try:
    response = blogs_table.scan()
    blogs = response.get('Items', [])
    return blogs
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/blogs/{blog_id}")
async def get_blog(blog_id: str):
  try:
    response = blogs_table.get_item(Key={'id': blog_id})
    blog = response.get('Item')
    if not blog:
      raise HTTPException(status_code=404, detail="Blog not found")
    return blog
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/blogs")
async def add_blog(blog: Blog):
  try:
    blogs_table.put_item(Item=blog.dict())
    return {"message": "Blog added successfully!"}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.delete("/api/blogs/{blog_id}")
async def delete_blog(blog_id: str):
  try:
    blogs_table.delete_item(Key={'id': blog_id})
    return {"message": "Blog deleted successfully!"}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))