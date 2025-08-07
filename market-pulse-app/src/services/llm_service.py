async def get_market_pulse(ticker: str, momentum: dict, news: list):
    score = momentum["score"]
    news_titles = [n["title"] for n in news]

    if score > 0.2 and "earnings" in " ".join(news_titles).lower():
        pulse = "bullish"
    elif score < -0.2:
        pulse = "bearish"
    else:
        pulse = "neutral"

    explanation = (
        f"Momentum score is {score}. News headlines suggest sentiment. Hence {pulse}."
    )
    return pulse, explanation