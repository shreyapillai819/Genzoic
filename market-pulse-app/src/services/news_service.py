import httpx
import os
from utils.cache import cache
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

@cache(ttl=600)
async def fetch_news(ticker: str):
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        articles = data.get("articles", [])

    return [
        {
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "url": article.get("url", "")
        }
        for article in articles
    ]
