"ER diagram: https://lucid.app/lucidchart/7307b97d-fb32-456c-96c9-886c6a0f9bc2/edit?beaconFlowId=189C3E30DE5B2368&invitationId=inv_7a8b60ce-3745-4b11-a220-dc4d8fbe4d0e&page=0_0#"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./air_quality.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()