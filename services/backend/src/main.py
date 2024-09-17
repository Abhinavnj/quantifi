from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from blog_api import router as blog_router
from analysis_api import router as analysis_router

app = FastAPI()

origins = [
  "http://3.22.166.72",
  "http://localhost:8080",
  "http://localhost:5173",
  "http://quantifiapp.com",
  "http://www.quantifiapp.com",
  "http://3.22.166.72:8080",
  "https://quantifiapp.com",
  "https://www.quantifiapp.com",
  "https://3.22.166.72:8080"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(blog_router)
app.include_router(analysis_router)

@app.get("/")
def home():
  return "Hello, World! - Quantifi :)"