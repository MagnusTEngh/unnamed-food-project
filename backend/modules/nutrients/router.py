from fastapi import APIRouter, Depends, HTTPException
from core.database import get_db
from sqlalchemy.orm import Session

from .models import Nutrient
from .schemas import NutrientItem

router = APIRouter(prefix="/nutrients", tags=["nutrients"])

@router.get("/", response_model=list[NutrientItem])
def get_nutrient_by_name(db: Session = Depends(get_db)):
    nutrient = db.query(Nutrient).all()
    if nutrient:
        return nutrient
    raise HTTPException(status_code=404, detail="Nutrient not found")


@router.get("/{name}", response_model=NutrientItem)
def get_nutrient_by_name(name: str, db: Session = Depends(get_db)):
    nutrient = db.query(Nutrient).filter(Nutrient.name == name).first()
    if nutrient:
        return nutrient
    raise HTTPException(status_code=404, detail="Nutrient not found")
