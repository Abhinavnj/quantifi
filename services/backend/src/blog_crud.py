# BLOG API
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import boto3
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')  # Default to 'us-east-1' if not set

# Initialize DynamoDB
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Initialize the table and verify existence
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
# try:
#   table = dynamodb.create_table(
#     TableName='Blogs',
#     KeySchema=[
#       {
#       'AttributeName': 'itemId',
#       'KeyType': 'HASH'
#       }
#     ],
#     AttributeDefinitions=[
#       {
#       'AttributeName': 'itemId',
#       'AttributeType': 'S'
#       }
#     ],
#     ProvisionedThroughput={
#       'ReadCapacityUnits': 1,
#       'WriteCapacityUnits': 1
#     }
#   )
#   print("Table status:", table.table_status)
# except Exception as e:
#   print('error', e)

try:
    blogs_table = dynamodb.Table('Blogs')
    # Optional: You can describe the table to verify it exists
    blogs_table.load()  # This triggers an API call to verify if the table exists
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        raise HTTPException(status_code=500, detail="DynamoDB table 'Blogs' not found.")
    else:
        raise

# Create a FastAPI router for blog-related endpoints
router = APIRouter()

# Blog model for adding/updating blogs
class Blog(BaseModel):
    itemId: str
    title: str
    description: str
    date: str  # YYYY-MM-DD format
    content: str

# API endpoint to get all blogs
@router.get("/api/blogs")
async def get_all_blogs():
    try:
        response = blogs_table.scan()
        blogs = response.get('Items', [])
        return blogs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get a blog by id
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

# API endpoint to add a new blog
@router.post("/api/blogs")
async def add_blog(blog: Blog):
    try:
        blogs_table.put_item(Item=blog.dict())
        return {"message": "Blog added successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to delete a blog by id
@router.delete("/api/blogs/{blog_id}")
async def delete_blog(blog_id: str):
    try:
        blogs_table.delete_item(Key={'id': blog_id})
        return {"message": "Blog deleted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))