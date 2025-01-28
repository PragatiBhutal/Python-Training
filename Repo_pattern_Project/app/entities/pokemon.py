from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    height = Column(Integer)
    weight = Column(Integer)
    xp = Column(Integer)
    image_url = Column(String)
    pokemon_url = Column(String)
    abilities = Column(JSON, nullable=True)
    stats = Column(JSON, nullable=True)
    types = Column(JSON, nullable=True)
