from sqlalchemy import Column, Integer, String
from db import Base


class CountryModel(Base):

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    region = Column(String, nullable=True)
    city_name = Column(String, nullable=True)
    language = Column(String, nullable=True)
    time = Column(Integer, nullable=False)


class TimeModel(Base):

    __tablename__ = "times"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(Integer)
    minimum = Column(Integer)
    maximum = Column(Integer)
    avg = Column(Integer)