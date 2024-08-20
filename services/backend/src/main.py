from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

from src.routes import users, notes

import requests

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:8080", "http://localhost:5173"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(notes.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)
api_key = "on4ayqQH6Wn1sT8yPwtsydDWRZDxFSqJ"

@app.get("/")
def home():
  return "Hello, World!"

@app.get("/test")
def home():
  return "Test!"
  
@app.get("/api/symbol_search")
def symbol_search(keywords: str):
  
  # url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={api_key}"
  url = f"https://api.polygon.io/v3/reference/tickers?search={keywords}&active=true&limit=10&apiKey={api_key}"
  response = requests.get(url)
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail="Error fetching data")
  return response.json()

@app.get("/api/ticker/open_close")
def ticker_open_close(ticker: str):
  if not ticker:
      raise HTTPException(status_code=400, detail="Ticker symbol is required")
  
  url = f"https://api.polygon.io/v1/open-close/{ticker}/previous?adjusted=true&apiKey={api_key}"
  
  try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()
      return {
          "open": data.get("open"),
          "close": data.get("close"),
      }
  except requests.exceptions.RequestException as e:
      raise HTTPException(status_code=500, detail=str(e))
