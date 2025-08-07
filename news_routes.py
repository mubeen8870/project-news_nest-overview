from fastapi import APIRouter, HTTPException
from schemas import News
from external_service import fetch_live_news
import json

router = APIRouter()
DB_FILE = "database.json"

def load_data():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

@router.post("/news/")
def create_news(news: News):
    data = load_data()
    data.append(news.dict())
    save_data(data)
    return {"message": "News added successfully"}

@router.get("/news/")
def get_all_news():
    return load_data()

@router.get("/news/{news_id}")
def get_news_by_id(news_id: int):
    data = load_data()
    for item in data:
        if item["id"] == news_id:
            return item
    raise HTTPException(status_code=404, detail="News not found")

@router.put("/news/{news_id}")
def update_news(news_id: int, news: News):
    data = load_data()
    for index, item in enumerate(data):
        if item["id"] == news_id:
            data[index] = news.dict()
            save_data(data)
            return {"message": "News updated"}
    raise HTTPException(status_code=404, detail="News not found")

@router.delete("/news/{news_id}")
def delete_news(news_id: int):
    data = load_data()
    for item in data:
        if item["id"] == news_id:
            data.remove(item)
            save_data(data)
            return {"message": "News deleted"}
    raise HTTPException(status_code=404, detail="News not found")

@router.get("/news/search/")
def search_news(title: str):
    data = load_data()
    result = [item for item in data if title.lower() in item["title"].lower()]
    return result

@router.get("/news/count/")
def count_news():
    data = load_data()
    return {"count": len(data)}

@router.get("/news/live/")
def get_live_news():
    return fetch_live_news()
