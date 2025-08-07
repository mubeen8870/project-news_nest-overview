from fastapi import FastAPI
from news_routes import router as news_router

app = FastAPI(title="NewsNest - FastAPI News Manager")

app.include_router(news_router)