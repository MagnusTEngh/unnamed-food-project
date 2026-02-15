import requests
import json
import logging

from sqlalchemy.exc import IntegrityError

from core.database import SessionLocal
from modules.nutrients.schemas import NutrientItem
from modules.nutrients.models import Nutrient
from modules.food.schemas import FoodItem, FoodNutritionItem, FoodMeasurementItem
from modules.food.models import Food, FoodNutrition, FoodMeasurements

logger = logging.getLogger(__name__)

SOURCE = "Matvaretabellen"
URL_BASE = "https://www.matvaretabellen.no/api"
LANGUAGE = "en"

NUTRIENTS = None
FOODS = None


def send_request(url):
    logger.debug(f"Sending request to url: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        logger.debug("Success!")
        return response
    else:
        logger.warning(f"Response from {url}: {response.status_code}")


def collect_json_data():
    global NUTRIENTS, FOODS
    url = f"{URL_BASE}/{LANGUAGE}/nutrients.json"
    response = send_request(url)
    NUTRIENTS = response.json()["nutrients"]
    url = f"{URL_BASE}/{LANGUAGE}/foods.json"
    response = send_request(url)
    FOODS = response.json()["foods"]


def get_nutrients():
    global NUTRIENTS

    for nutrient in NUTRIENTS:
        nutrient = NutrientItem(name=nutrient["name"], measured_in=nutrient["unit"])
        db = SessionLocal()
        try:
            db.add(Nutrient(name=nutrient.name, measured_in=nutrient.measured_in))
            db.commit()
        except IntegrityError as e:
            db.rollback()
            logger.warning(f"IntegrityError for nutrient '{nutrient.name}': {e.orig}")
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()


def get_foods():
    global FOODS, NUTRIENTS, SOURCE

    nutrient_mapping = {item["nutrientId"]: item["name"] for item in NUTRIENTS}

    print(FOODS[0])
    food = FOODS[0]

    db = SessionLocal()
    try:
        fooditem = FoodItem(
            source=SOURCE,
            owned_by="App",
            name=food["foodName"],
            default_measurement="To be determined",
        )
        db.add(
            Food(
                source=fooditem.source,
                owned_by=fooditem.owned_by,
                name=fooditem.name,
                default_measurement=fooditem.default_measurement,
            )
        )
        db.commit()
    except IntegrityError as e:
        db.rollback()
        logger.warning(f"IntegrityError for food '{fooditem.name}")
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
    for nutrient in food["constituents"]:
        if "quantity" not in nutrient.keys():
            continue
        db = SessionLocal()
        try:
            nutrition_item = FoodNutritionItem(
                food=food["foodName"],
                nutrient=nutrient_mapping[nutrient["nutrientId"]],
                measurement=nutrient["unit"],
                amount=nutrient["quantity"],
            )
            db.add(
                FoodNutrition(
                    food=nutrition_item.food,
                    nutrient=nutrition_item.nutrient,
                    measurement=nutrition_item.measurement,
                    amount=nutrition_item.amount,
                )
            )
            db.commit()
        except IntegrityError as e:
            db.rollback()
            logger.warning(f"IntegrityError for food '{fooditem.name} when trying to insert nutrient '{nutrition_item.nutrient}'")
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    # for food in response.json()["foods"]:


"""    db = SessionLocal()
    try:
        ...
    except IntegrityError as e:
        db.rollback()
        logger.warning()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()"""

if __name__ == "__main__":
    collect_json_data()
    # get_nutrients()
    get_foods()
