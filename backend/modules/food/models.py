from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Food(Base):
    __tablename__ = "food"
    id = Column(Integer, autoincrement=True)
    source = Column(String, primary_key=True)  # an API source or the username
    owned_by = Column(String)  # Who created the entry.
    name = Column(String, primary_key=True)
    default_measurement = Column(String)


class FoodNutrition(Base):
    __tablename__ = "foodnutrition"
    food = Column(String, ForeignKey("food.name"))
    nutrient = Column(String, ForeignKey("nutrient.name"))
    measurement = Column(String)  # Valid options should be defined by chosen nutrient.
    amount = Column(Float)


class FoodMeasurements(Base):
    """Keeps information about different measures for amount of food and conversion ratio to a default measurement."""

    __tablename__ = "foodmeasurements"
    food = Column(String, ForeignKey("food.name"), primary_key=True)
    base_measurement = food = Column(String, ForeignKey("food.default_measurement"))
    measurement = Column(String, primary_key=True)
    value = Column(Float)
