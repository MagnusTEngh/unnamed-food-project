import json
from pydantic import BaseModel

from .models import Food, FoodNutrition, FoodMeasurements

class FoodItem(BaseModel):
    source: str
    owned_by: str
    name: str
    default_measurement: str

    def to_sqlalchemy(self):
        return Food(
            source=self.source,
            owned_by = self.owned_by,
            name = self.name,
            default_measurement = self.default_measurement
        )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(\n"
            + json.dumps(self.model_dump(), indent=2)
            + "\n)"
        )

class FoodNutritionItem(BaseModel):
    food: str
    nutrient: str
    measurement: str
    amount: float

    def to_sqlalchemy(self, source):
        FoodNutrition(
            source = source,
            food = self.food,
            nutrient = self.nutrient,
            measurement = self.measurement,
            amount = self.amount
        )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(\n"
            + json.dumps(self.model_dump(), indent=2)
            + "\n)"
        )


class FoodMeasurementItem(BaseModel):
    food: str
    base_measurement: str
    measurement: str
    value: str

    def to_sqlalchemy(self, source):
        FoodMeasurements(
            source=source,
            food = self.food,
            base_measurement = self.base_measurement,
            measurement=self.measurement,
            value = self.value
        )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(\n"
            + json.dumps(self.model_dump(), indent=2)
            + "\n)"
        )
