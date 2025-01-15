from fastapi import APIRouter, Depends, HTTPException, Response
from schema import RentalDisplaySchema, RentalCreateSchema
from typing import List
from database import get_db
from sqlalchemy.orm import Session
from models import RentalModel

router = APIRouter()

@router.get("/", response_model=List[RentalDisplaySchema])
def get_rentals(db: Session = Depends(get_db)): #récupère le yield de get_db dans database
    db_rentals = db.query(RentalModel)
    return db_rentals

@router.post("/", response_model=RentalDisplaySchema)
def create_reantal(rental: RentalCreateSchema, db: Session = Depends(get_db)):
    db_rental = RentalModel(**rental.model_dump())
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental
