from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql:///?User=root&Password=pass&Database=AirQuality&Server=myServer&Port=3306"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})