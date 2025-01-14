from fastapi import APIRouter, Depends
from schema import Car, CarCreate
from typing import List
from database import get_db
from sqlalchemy.orm import Session
from models import Car as CarModel

router = APIRouter()

@router.get("/", response_model=List[Car])
def get_cars(db: Session = Depends(get_db)): #récupère le yield de get_db dans database
    db_cars = db.query(CarModel)
    return db_cars

@router.get("/{car_id}", response_model=Car)
def get_car_by_id(car_id:int, db: Session = Depends(get_db)):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    return db_car

@router.post("/", response_model=Car)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = CarModel(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car