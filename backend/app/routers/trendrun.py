from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import TrendRun
from app.schemas import TrendRunCreate, TrendRunOut
from typing import List

router = APIRouter(
    prefix="/api/trends",
    tags=["trends"]
)


@router.post("/", response_model=TrendRunOut)
def create_trend(trend: TrendRunCreate, db: Session = Depends(get_db)):
    db_trend = TrendRun(
        trend1=trend.trend1,
        trend2=trend.trend2,
        trend3=trend.trend3,
        trend4=trend.trend4,
        trend5=trend.trend5,
        finished_at=trend.finished_at,
        ip_address=trend.ip_address
    )
    db.add(db_trend)
    db.commit()
    db.refresh(db_trend)
    return db_trend



@router.get("/", response_model=List[TrendRunOut])
def read_trends(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    trends = db.query(TrendRun).offset(skip).limit(limit).all()
    return trends



@router.get("/{trend_id}", response_model=TrendRunOut)
def read_trend(trend_id: int, db: Session = Depends(get_db)):
    db_trend = db.query(TrendRun).filter(TrendRun.id == trend_id).first()
    if not db_trend:
        raise HTTPException(status_code=404, detail="Trend not found")
    return db_trend
