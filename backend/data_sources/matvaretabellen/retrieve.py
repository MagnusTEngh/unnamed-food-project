import requests
import json
import logging

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
    nutrient = response.json()["nutrients"][0]
    nutrient = NutrientItem(name=nutrient["name"], measured_in=nutrient["unit"])
    db = SessionLocal()
    try:
        nutrient_to_add = Nutrient(
            name = nutrient.name,
            measured_in = nutrient.measured_in
        )
        db.add(nutrient_to_add)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
    

if __name__ == "__main__":
    get_nutrients()