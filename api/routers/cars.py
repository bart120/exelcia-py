from fastapi import APIRouter
from schema import Car, CarCreate
#from schemas.car import Car
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Car])
def get_cars():
    return []

@router.get("/{car_id}", response_model=Car)
def get_car_by_id(car_id:int):
    return {}

@router.post("/", response_model=Car)
def create_car(car: CarCreate):
    resp = Car(**car.model_dump(), id=0)
    return resp