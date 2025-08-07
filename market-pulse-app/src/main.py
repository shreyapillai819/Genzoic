from fastapi import FastAPI, Query
from services.price_service import fetch_price_momentum
from services.news_service import fetch_news
from services.llm_service import get_market_pulse
from models.schema import MarketPulseResponse
from datetime import date

app = FastAPI()

@app.get("/api/v1/market-pulse", response_model=MarketPulseResponse)
async def market_pulse(ticker: str = Query(...)):
    momentum = await fetch_price_momentum(ticker)
    news = await fetch_news(ticker)
    pulse, explanation = await get_market_pulse(ticker, momentum, news)

    return {
        "ticker": ticker.upper(),
        "as_of": str(date.today()),
        "momentum": momentum,
        "news": news,
        "pulse": pulse,
        "llm_explanation": explanation
    }