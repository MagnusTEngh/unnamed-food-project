from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey, ForeignKeyConstraint, UniqueConstraint

from db.base import Base


class Food(Base):
    __tablename__ = "food"
    id = Column(Integer, autoincrement=True)
    source = Column(String, primary_key=True)  # an API source or the username
    owned_by = Column(String)  # Who created the entry.
    name = Column(String, primary_key=True)
    default_measurement = Column(String)

    __table_args__ = (
        UniqueConstraint("source", "name", "default_measurement"),
    )


class FoodNutrition(Base):
    __tablename__ = "foodnutrition"
    source = Column(String, primary_key=True)
    food = Column(String, primary_key=True)
    nutrient = Column(String, ForeignKey("nutrient.name"), primary_key=True)
    measurement = Column(String)  # Valid options should be defined by chosen nutrient.
    amount = Column(Float)
    
    __table_args__ = (
        ForeignKeyConstraint(
            ["source", "food"],
            ["food.source", "food.name"]
        ),
    )


class FoodMeasurements(Base):
    """Keeps information about different measures for amount of food and conversion ratio to a default measurement."""

    __tablename__ = "foodmeasurements"
    source = Column(String, primary_key=True)
    food = Column(String, primary_key=True)
    base_measurement = Column(String, primary_key=True)
    measurement = Column(String, primary_key=True)
    value = Column(Float)

    __table_args__ = (
        ForeignKeyConstraint(
            ["source", "food", "base_measurement"],
            ["food.source", "food.name", "food.default_measurement"]
        ),
    )
