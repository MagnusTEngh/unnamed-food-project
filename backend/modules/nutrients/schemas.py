import json
from pydantic import BaseModel

class NutrientItem(BaseModel):
    name: str
    measured_in: str

    def __str__(self):
        return (
            f"{self.__class__.__name__}(\n"
            + json.dumps(self.model_dump(), indent=2)
            + "\n)"
        )
