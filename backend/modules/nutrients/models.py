from sqlalchemy import Column, Integer, String, create_engine


from db.base import Base


class Nutrient(Base):
    __tablename__ = "nutrient"
    name = Column(String, primary_key=True)
    measured_in = Column(String)
