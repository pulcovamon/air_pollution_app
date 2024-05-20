from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'sqlite:///./db/air_quality.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

def get_db():
    Session = sessionmaker(bind=engine)
    db = Session()
    try:
        yield db
    finally:
        db.close()