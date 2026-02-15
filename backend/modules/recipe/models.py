from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipe"
    id = Column(Integer, autoincrement=True)
    name = Column(String, primary_key=True)
    created_by = Column(String, primary_key=True)
    description = Column(String)


class RecipeIngredients(Base):
    __tablename__ = "recipeingredients"
    recipe = Column(String, ForeignKey("recipe.id"))
    food = Column(String, ForeignKey("food.name"))
    measure = Column(String)
    amount = Column(Float)