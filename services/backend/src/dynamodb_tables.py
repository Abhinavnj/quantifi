import boto3
import os
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from fastapi import HTTPException

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
# dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)

def get_table(table_name):
  try:
    table = dynamodb.Table(table_name)
    table.load()  # This triggers an API call to verify if the table exists
  except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
      raise HTTPException(status_code=500, detail="DynamoDB table 'Blogs' not found.")
    else:
      raise
    
  return table