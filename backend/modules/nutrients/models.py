from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Nutrient(Base):
    __tablename__ = "nutrient"
    name = Column(String, primary_key=True)
    measured_in = Column(String)
