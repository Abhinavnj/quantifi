from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv

# import routers
from blog_api import router as blog_router
from analysis_api import router as analysis_router

load_dotenv()
app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://3.22.166.72", "http://localhost:8080", "http://localhost:5173", "http://quantifiapp.com", "http://www.quantifiapp.com", "http://3.22.166.72:8080", "https://quantifiapp.com", "https://www.quantifiapp.com", "https://3.22.166.72:8080"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(blog_router)
app.include_router(analysis_router)

@app.get("/")
def home():
  return "Hello, World! - Quantifi :)"

@app.get("/api/symbol_search")
def symbol_search(keywords: str):
  url = f"https://api.polygon.io/v3/reference/tickers?search={keywords}&active=true&limit=10&apiKey={polygon_api_key}"
  response = requests.get(url)
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail="Error fetching data")
  return response.json()