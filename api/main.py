from fastapi import FastAPI
from routers import cars, rentals
from database import base, engine

app = FastAPI()

base.metadata.create_all(bind=engine)# génère les structures en bdd

app.include_router(cars.router, prefix="/cars")
app.include_router(rentals.router, prefix="/rentals")

@app.get("/")
def read_root():
    return {"message":"Coucou!!"}