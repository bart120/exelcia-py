from pydantic import BaseModel, field_validator, Field
from typing import Optional
import re
from datetime import datetime

class CarParent(BaseModel):
    brand: str
    model: str 
    daily_rate: Optional[float] = None
    create_dt: datetime

    @field_validator("model")
    def validate_model(cls, value):
        if len(value) < 3:
            raise ValueError("Le model doit contenir 3 caractères minimum")
        pattern = r"^[A-Za-z]*$"
        if not re.match(pattern, value):
            raise ValueError("Le model doit contenir que des caractères ")
        return value


class Car(CarParent):
    id:int
    full_name: str
    
class CarCreate(CarParent):
    pass

class RentalParentSchema(BaseModel):
    start_date: datetime
    end_date: datetime
    total_cost: float
    car_id: int

class RentalDisplaySchema(RentalParentSchema):
    id:int
    car:Car
    class Config:
        orm_mode = True

class RentalCreateSchema(RentalParentSchema):
    pass

