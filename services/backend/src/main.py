from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import time
from dotenv import load_dotenv
from threading import Lock

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://3.22.166.72", "http://localhost:8080", "http://localhost:5173", "http://quantifiapp.com", "http://www.quantifiapp.com", "http://3.22.166.72:8080", "https://quantifiapp.com", "https://www.quantifiapp.com", "https://3.22.166.72:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

polygon_api_key = os.getenv('POLYGON_API_KEY')

# Cache dictionary with expiration and a lock for thread safety
cache = {}
cache_lock = Lock()
CACHE_EXPIRATION_SECONDS = 300  # Cache entries expire after 5 minutes

@app.get("/")
def home():
    return "Hello, World!"

@app.get("/test")
def home():
    return "Test!"

@app.get("/api/symbol_search")
def symbol_search(keywords: str):
    url = f"https://api.polygon.io/v3/reference/tickers?search={keywords}&active=true&limit=10&apiKey={polygon_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    return response.json()

@app.get("/api/ticker/details")
def ticker_details(ticker: str):
    print("GETTING DETAILS")
  
    if not ticker:
        raise HTTPException(status_code=400, detail="Ticker symbol is required")
    
    # Thread-safe cache read
    with cache_lock:
        if ticker in cache and "details" in cache[ticker]:
            entry = cache[ticker]["details"]
            if time.time() - entry["timestamp"] < CACHE_EXPIRATION_SECONDS:
                return entry["data"]
            else:
                # Cache expired, remove the entry
                del cache[ticker]["details"]
    
    # Make API call if not in cache or cache expired
    url = f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    
    # Store details in the cache with a timestamp
    with cache_lock:
        if ticker not in cache:
            cache[ticker] = {}
        cache[ticker]["details"] = {
            "data": response.json()["results"],
            "timestamp": time.time()
        }
    
    return cache[ticker]["details"]["data"]

@app.get("/api/ticker/financials")
def ticker_financials(ticker: str):
    if not ticker:
        raise HTTPException(status_code=400, detail="Ticker symbol is required")
    
    # Thread-safe cache read
    with cache_lock:
        if ticker in cache and "financials" in cache[ticker]:
            entry = cache[ticker]["financials"]
            if time.time() - entry["timestamp"] < CACHE_EXPIRATION_SECONDS:
                return entry["data"]
            else:
                # Cache expired, remove the entry
                del cache[ticker]["financials"]
    
    # Make API call if not in cache or cache expired
    url = f"https://api.polygon.io/vX/reference/financials?ticker={ticker}&limit=10&apiKey={polygon_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    
    # Store financials in the cache with a timestamp
    with cache_lock:
        if ticker not in cache:
            cache[ticker] = {}
        cache[ticker]["financials"] = {
            "data": response.json()["results"],
            "timestamp": time.time()
        }
    
    return cache[ticker]["financials"]["data"]

@app.get("/api/ticker/prev_close")
def ticker_prev_close(ticker: str):
	if not ticker:
		raise HTTPException(status_code=400, detail="Ticker symbol is required")
	
	url = f"https://api.polygon.io/v2/aggs/ticker/{(str(ticker)).upper()}/prev?adjusted=true&apiKey={polygon_api_key}"
	response = requests.get(url)
	if response.status_code != 200:
		raise HTTPException(status_code=response.status_code, detail="Error fetching data")
	return response.json()["results"][0]['c']

def ticker_snapshot(ticker: str):
  url = f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{(str(ticker)).upper()}?apiKey={polygon_api_key}"
  response = requests.get(url)
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail="Error fetching data")
  return response.json()

# @app.get("/api/analysis/ticker")
# def ticker_analysis(ticker: str):
#   if not ticker:
#     raise HTTPException(status_code=400, detail="Ticker symbol is required")
  
#   try:
#     snapshot = ticker_snapshot(ticker)
    
#   except Exception:
#     print("analysis issue")
  
#   details = ticker_details(ticker)
#   print("details", details)
  
#   data = {}
#   data['name'] = details.get("name", "Name not found")
#   data['logo'] = details["branding"]["icon_url"] + '?' + "apiKey=" + polygon_api_key
#   data['close'] = snapshot["ticker"]["day"]["c"]
#   data['open'] = snapshot["ticker"]["day"]["o"]
  
#   print(data)
  
#   return data

import base64

@app.get("/api/analysis/ticker")
def ticker_analysis(ticker: str):
    if not ticker:
        raise HTTPException(status_code=400, detail="Ticker symbol is required")

    try:
        snapshot = ticker_snapshot(ticker)
        details = ticker_details(ticker)

        # Fetch logo and encode it as base64
        logo_url = details["branding"]["icon_url"] + '?' + "apiKey=" + polygon_api_key
        logo_response = requests.get(logo_url)

        if logo_response.status_code == 200:
            logo_base64 = base64.b64encode(logo_response.content).decode('utf-8')
        else:
            logo_base64 = None

        data = {
            'name': details.get("name", "Name not found"),
            'close': snapshot["ticker"]["day"]["c"],
            'open': snapshot["ticker"]["day"]["o"],
            'logo_base64': f"data:image/png;base64,{logo_base64}" if logo_base64 else None
        }

        return data

    except Exception as e:
        print("Error during analysis:", e)
        raise HTTPException(status_code=500, detail="Server error")
