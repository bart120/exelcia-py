from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from secret_manager import get_secret

value_password = get_secret("db_password_key", "1")

DATABASE_URL = f"mysql+mysqlconnector://vincent:{value_password}@34.133.229.240/exelcia-api"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
base = declarative_base()



def get_db():
    db= session_local()
    try:
        yield db
    finally:
        db.close()