from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base

from config.db import engine

Base = declarative_base()


class Clothe(Base):
    __tablename__ = "clothes"
    id = (Column(Integer, primary_key=True))
    tipo = (Column(String(250)))
    talla = (Column(String(250)))
    color = (Column(String(250)))
    material = (Column(String(250)))
    marca = (Column(String(250)))
    condicion = (Column(String(250)))
    precio = (Column(Float))
    disponible = Column(Boolean, default=True)


Base.metadata.create_all(engine)
