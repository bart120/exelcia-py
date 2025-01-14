from fastapi import FastAPI
from routers import cars
from database import base, engine

app = FastAPI()

base.metadata.create_all(bind=engine)# génère les structures en bdd

app.include_router(cars.router, prefix="/cars")

@app.get("/")
def read_root():
    return {"message":"Coucou!!"}