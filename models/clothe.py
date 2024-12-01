from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base

from config.db import engine

Base = declarative_base()

class Clothe(Base):
    __tablename__ = "clothes"
    id = (Column(Integer, primary_key=True))
    type = Column(String(25), nullable=True)
    size = Column(String(25))
    color = Column(String(25), nullable=True)
    img_url = Column(String(500))
    condition = Column(String(25), nullable=True)
    brand = Column(String(25), nullable=True)
    price = Column(Float)
    available = Column(Boolean, default=True, nullable=True)


Base.metadata.create_all(engine)
