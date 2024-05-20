from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .db_connection import engine
from .models import AirQualityIndex, Parameter, Statistics, CityComparison

app = FastAPI()

@app.get("/cities", response_model=List[models.City])
async def read_cities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cities = db.query(models.City).offset(skip).limit(limit).all()
    return cities

@app.get("/air_quality_index/{city_id}", response_model=List[schemas.AirQualityIndex])
async def read_air_quality_index(city_id: int, db: Session = Depends(get_db)):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=30)
    aqi = db.query(models.AirQualityIndex).filter(
        models.AirQualityIndex.city_id == city_id,
        models.AirQualityIndex.date >= start_date,
        models.AirQualityIndex.date <= end_date
    ).all()
    if not aqi:
        raise HTTPException(status_code=404, detail="Air quality index not found")
    return aqi

@app.get("/air_quality_parameters/{city_id}", response_model=List[schemas.Parameter])
async def read_air_quality_parameters(city_id: int, db: Session = Depends(get_db)):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=30)
    params = db.query(models.Parameter).filter(
        models.Parameter.city_id == city_id,
        models.Parameter.date >= start_date,
        models.Parameter.date <= end_date
    ).all()
    if not params:
        raise HTTPException(status_code=404, detail="Air quality parameters not found")
    return params

@app.get("/statistics/{city_id}", response_model=models.Statistics)
async def read_statistics(city_id: int, db: Session = Depends(get_db)):
    statistics = db.query(models.Statistics).filter(models.Statistics.city_id == city_id).first()
    if not statistics:
        raise HTTPException(status_code=404, detail="Statistics not found")
    return statistics

@app.get("/city_comparison", response_model=List[models.CityComparison])
async def read_city_comparison(db: Session = Depends(get_db)):
    comparison = db.query(models.CityComparison).all()
    return comparison