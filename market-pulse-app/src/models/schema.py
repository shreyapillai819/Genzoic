from pydantic import BaseModel
from typing import List

class NewsItem(BaseModel):
    title: str
    description: str
    url: str

class MomentumData(BaseModel):
    returns: List[float]
    score: float

class MarketPulseResponse(BaseModel):
    ticker: str
    as_of: str
    momentum: MomentumData
    news: List[NewsItem]
    pulse: str
    llm_explanation: str