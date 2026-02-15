import requests
import json
import logging

from sqlalchemy.exc import IntegrityError

from core.database import SessionLocal
from modules.nutrients.schemas import NutrientItem
from modules.nutrients.models import Nutrient

logger = logging.getLogger(__name__)
URL_BASE = "https://www.matvaretabellen.no/api"

LANGUAGE = "en"

def send_request(url):
    logger.debug(f"Sending request to url: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        logger.debug("Success!")
        return response
    else:
        logger.warning(f"Response from {url}: {response.status_code}")

def get_nutrients():
    url = f"{URL_BASE}/{LANGUAGE}/nutrients.json"
    response = send_request(url)
    for nutrient in response.json()["nutrients"]:
        nutrient = NutrientItem(name=nutrient["name"], measured_in=nutrient["unit"])
        db = SessionLocal()
        try:
            nutrient_to_add = Nutrient(
                name = nutrient.name,
                measured_in = nutrient.measured_in
            )
            db.add(nutrient_to_add)
            db.commit()
        except IntegrityError as e:
            db.rollback()
            logger.warning(f"IntegrityError for nutrient '{nutrient.name}': {e.orig}")
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    

if __name__ == "__main__":
    get_nutrients()