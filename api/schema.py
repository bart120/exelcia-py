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
    
class CarCreate(CarParent):
    pass