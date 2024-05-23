from sqlmodel import create_engine, Session

DATABASE_URL = "mysql+mysqlconnector://user:pass@db:3306/AirQuality"

engine = create_engine(DATABASE_URL)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()