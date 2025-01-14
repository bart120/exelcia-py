from pydantic import BaseModel

class Car(BaseModel):
    id:int
    brand: str
    model: str
    daily_rate: float