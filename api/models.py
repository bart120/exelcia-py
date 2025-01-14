from database import base
from sqlalchemy import Column, Integer, String, Float, DateTime

class Car(base):
    __tablename__ ="cars"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(150), nullable=False)
    model = Column(String(150), nullable=False)
    daily_rate = Column(Float, nullable=True)
    create_dt = Column(DateTime, nullable=False)
    
