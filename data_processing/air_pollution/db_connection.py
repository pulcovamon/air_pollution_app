from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://user:pass@0.0.0.0:3306/AirQuality"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})