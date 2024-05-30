from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .db_connection import engine, get_db
from . import models

app = APIRouter()

@app.get("/cities")
async def read_cities(db: Session = Depends(get_db)):
    cities = db.query(models.City).all()
    json_compatible_item_data = jsonable_encoder(cities)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/air_quality_index/{city_id}", response_model=List[models.AirQualityIndex])
async def read_air_quality_index(city_id: int, db: Session = Depends(get_db)):
    start_date = datetime.now() - timedelta(days=30)
    aqi = db.query(models.AirQualityIndex).filter(
        models.AirQualityIndex.city_id == city_id,
        models.AirQualityIndex.date >= start_date,
    ).all()
    if not aqi:
        raise HTTPException(status_code=404, detail="Air quality index not found")
    return aqi

@app.get("/air_quality_parameters/{city_id}/{parameter}", response_model=List[models.Parameter])
async def read_air_quality_parameters(city_id: int, parameter: str, db: Session = Depends(get_db)):
    start_date = datetime.now() - timedelta(days=30)
    params = db.query(models.Parameter).filter(
        models.Parameter.city_id == city_id,
        models.Parameter.pollutant == parameter,
        models.Parameter.date >= start_date,
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

@app.get("/city_comparison")
async def read_city_comparison(db: Session = Depends(get_db)):
    comparisons = db.query(models.CityComparison).all()
    results = []
    for comparison in comparisons:
        city = db.scalars(select(models.City).where(models.City.id==comparison.city_id)).one()
        statistics = db.scalars(select(models.Statistics).where(models.Statistics.city_id==comparison.city_id)).one()
        result = {
            "id": comparison.id,
            "city_id": comparison.city_id,
            "index": comparison.index,
            "city_name": None if not city else city.name,
            "mean": None if not statistics else statistics.month_avg
        }
        results.append(result)
    return results