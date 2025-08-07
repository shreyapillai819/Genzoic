import random
from utils.cache import cache

@cache(ttl=600)
async def fetch_price_momentum(ticker: str):
    returns = [round(random.uniform(-1, 1), 2) for _ in range(5)]
    score = sum(returns) / len(returns)
    return {"returns": returns, "score": round(score, 2)}