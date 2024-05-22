from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://user:pass@0.0.0.0:3306/AirQuality"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

def get_db():
    Session = sessionmaker(bind=engine)
    db = Session()
    try:
        yield db
    finally:
        db.close()