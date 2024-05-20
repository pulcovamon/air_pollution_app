from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'sqlite:///./db/air_quality.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})