# 📊 Market-Pulse Microservice

> A 4-hour MVP prototype for Genzoic's coding assessment. It analyzes a stock's market sentiment (bullish / neutral / bearish) using real-time momentum and news signals, powered by FastAPI and React.

---

## 🔧 Tech Stack

| Layer     | Technology |
|-----------|------------|
| Backend   | Python (FastAPI), httpx, dotenv |
| Frontend  | React, Axios                     |
| Cache     | In-memory TTL cache (custom)     |
| APIs Used | Alpha Vantage (stock data), NewsAPI (news headlines) |

---

## 🚀 Features

- ✅ Fetches **last 5-day returns** from Alpha Vantage  
- ✅ Fetches **5 latest news headlines** from NewsAPI  
- ✅ Calculates a **simple momentum score**  
- ✅ Uses a **mocked LLM logic** to classify stock as `bullish`, `neutral`, or `bearish`  
- ✅ REST API: `/api/v1/market-pulse?ticker=MSFT`  
- ✅ React frontend: chat-style interface with result card + collapsible JSON  
- ✅ In-memory **TTL caching** (10 minutes)  

---

## Project Structure
market-pulse-app/
├── src/                          # 🔙 FastAPI backend
│   ├── main.py                   # Entry point for FastAPI app
│
│   ├── services/                 # Handles momentum, news, and pulse logic
│   │   ├── momentum.py
│   │   ├── news.py
│   │   └── pulse.py
│
│   ├── models/                   # Pydantic response models
│   │   └── response_model.py
│
│   ├── utils/                    # Caching and helper functions
│   │   └── cache.py
│
│   ├── .env                      # 🔑 API keys (not committed)
│   └── requirements.txt          # Python dependencies
│
└── frontend/                     # 🖥️ React frontend
    ├── src/
    │   └── App.js                # Main React component
    └── public/
        └── index.html            # Root HTML

