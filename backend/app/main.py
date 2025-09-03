from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import trendrun , scraper
from app.database import engine, create_db_and_tables


create_db_and_tables()

app = FastAPI(
    title="X-Trends Scraper API",
    description="API to manage trend scraping runs",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trendrun.router)
app.include_router(scraper.router)
