import json
from pydantic import BaseModel

class FoodItem(BaseModel):
    source: str
    owned_by: str
    name: str
    default_measurement: str

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

    def __str__(self):
        return (
            f"{self.__class__.__name__}(\n"
            + json.dumps(self.model_dump(), indent=2)
            + "\n)"
        )


class FoodMeasurementItem(BaseModel):
    source: str
    owned_by: str
    name: str
    default_measurement: str

    def __str__(self):
        return (
            f"{self.__class__.__name__}(\n"
            + json.dumps(self.model_dump(), indent=2)
            + "\n)"
        )
