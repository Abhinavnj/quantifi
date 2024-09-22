from fastapi import APIRouter, HTTPException
import requests
from datetime import timedelta
from datetime import datetime
import base64
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()
polygon_api_key = os.getenv('POLYGON_API_KEY')

def ticker_details(ticker: str):
  print("GETTING DETAILS")

  if not ticker:
    raise HTTPException(status_code=400, detail="Ticker symbol is required")

  # Make API call if not in cache or cache expired
  url = f"https://api.polygon.io/v3/reference/tickers/{ticker.upper()}?apiKey={polygon_api_key}"
  response = requests.get(url)
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail="Error fetching data")

  return response.json()["results"]

def ticker_snapshot(ticker: str):
  url = f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{(str(ticker)).upper()}?apiKey={polygon_api_key}"
  response = requests.get(url)
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail="Error fetching data")
  return response.json()

def fetch_aggregate_data(ticker: str):
  end_date = datetime.now().strftime('%Y-%m-%d')
  start_date = (datetime.now() - timedelta(days=5 * 365)).strftime('%Y-%m-%d')  # 5 years back
  url = f"https://api.polygon.io/v2/aggs/ticker/{ticker.upper()}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={polygon_api_key}"
  response = requests.get(url)
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail="Error fetching aggregate data")
  return response.json()["results"]

def ticker_news(ticker: str):
  if not ticker:
    raise HTTPException(status_code=400, detail="Ticker symbol is required")
  url = f"https://api.polygon.io/v2/reference/news?ticker={ticker.upper()}&limit=10&apiKey={polygon_api_key}"
  response = requests.get(url)
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail="Error fetching data")
  
  news = response.json()["results"]
  result = []
  for article in news:
    article_summary = {}
    article_summary['publisher_name'] = article["publisher"]["name"]
    article_summary['publisher_logo'] = article["publisher"]["logo_url"]
    article_summary['title'] = article["title"]
    article_summary['published_datetime'] = datetime.strptime(article["published_utc"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M")
    
    for insight in article["insights"]:
      if insight["ticker"].lower() == ticker.lower():
        article_summary['sentiment'] = insight["sentiment"]
        article_summary['sentiment_reasoning'] = insight["sentiment_reasoning"]
        break
    
    result.append(article_summary)
    
  return result

def ticker_financials(ticker: str):
  if not ticker:
    raise HTTPException(status_code=400, detail="Ticker symbol is required")

  # Make API call if not in cache or cache expired
  url = f"https://api.polygon.io/vX/reference/financials?ticker={ticker.upper()}&limit=10&apiKey={polygon_api_key}"
  response = requests.get(url)
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail="Error fetching data")
  
  result = response.json()["results"]
  if len(result) > 0:
    return result[0]
  
  return None

@router.get("/api/analysis")
def ticker_analysis(ticker: str):
    if not ticker:
        raise HTTPException(status_code=400, detail="Ticker symbol is required")

    try:
        snapshot = ticker_snapshot(ticker)
        details = ticker_details(ticker)
        financials = ticker_financials(ticker)
        
        if financials:
            financials = {
                'basic_earnings_per_share': financials["financials"]["income_statement"]["basic_earnings_per_share"]["value"]
            }
        else:
            financials = {}

        news = ticker_news(ticker)

        # Fetch logo and encode it as base64
        logo_url = details["branding"]["icon_url"] + '?' + "apiKey=" + polygon_api_key
        logo_response = requests.get(logo_url)

        if logo_response.status_code == 200:
            logo_base64 = base64.b64encode(logo_response.content).decode('utf-8')
        else:
            logo_base64 = None

        # Fetch aggregate data for the past 5 years
        aggregate_data = fetch_aggregate_data(ticker)

        # Adding 'info' alongside 'value' in overview section
        data = {
            'overview': {
                'name': {
                    'value': details.get("name", "Name not found"),
                    'info': "Company's official name"
                },
                'close': {
                    'value': snapshot["ticker"]["day"]["c"],
                    'info': "Price at which the stock closed today"
                },
                'open': {
                    'value': snapshot["ticker"]["day"]["o"],
                    'info': "Price at which the stock opened today"
                },
                'high': {
                    'value': snapshot["ticker"]["day"]["h"],
                    'info': "Highest price of the stock during the day"
                },
                'low': {
                    'value': snapshot["ticker"]["day"]["l"],
                    'info': "Lowest price of the stock during the day"
                },
                'todays_change': {
                    'value': f"{snapshot['ticker']['todaysChange']:+.2f}",
                    'info': "Difference between today's close and yesterday's close"
                },
                'todays_change_percentage': {
                    'value': f"{snapshot['ticker']['todaysChangePerc']:+.2f}%",
                    'info': "Percentage change in stock price from yesterday to today"
                },
                'last_minute_price': {
                    'value': snapshot["ticker"]["min"]["o"],
                    'info': "Stock price at the last minute of trading"
                },
                'logo_base64': {
                    'value': f"data:image/png;base64,{logo_base64}" if logo_base64 else None,
                    'info': "Company logo"
                }
            },
            'financials': financials,
            'news': news,
            'aggregate_data': aggregate_data
        }

        return data

    except Exception as e:
        print("Error during analysis:", e)
        raise HTTPException(status_code=500, detail="Server error")

  
@router.get("/api/symbol_search")
def symbol_search(keywords: str):
  url = f"https://api.polygon.io/v3/reference/tickers?search={keywords}&active=true&limit=10&apiKey={polygon_api_key}"
  response = requests.get(url)
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail="Error fetching data")
  return response.json()