import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CURRENT_DATE = datetime.now().strftime('%Y-%m-%d')
THREE_DAYS_AGO = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')

## API_KEYS & TOKENS
NEWS_API = os.getenv(key="NEWS_API")
TWILLIO_AUTH_TOKEN = os.getenv(key="TWILLIO_AUTH_TOKEN")
TWILLIO_ACCOUNT_SID = os.getenv(key="TWILLIO_ACCOUNT_SID")
TWILLIO_MESSAGE_SID=os.getenv(key="TWILLIO_MESSAGE_SID")

## URLS
VANTAGE_URL_FULL = os.getenv(key="VANTAGE_URL_FULL")
NEWS_URL = os.getenv(key="NEWS_URL")

## PHONE_NOS
MAIN_LINE = os.getenv("MAIN_LINE")
TWILLIO_LINE = os.getenv("TWILLIO_LINE")

## PARAMS
NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "from": CURRENT_DATE,
    "to": THREE_DAYS_AGO,
    "sortBy": "popularity",
    "apiKey": NEWS_API
}