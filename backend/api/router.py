from fastapi import APIRouter

#from modules.food.router import router as food_router
from modules.nutrients.router import router as nutrient_router
from modules.test.router import router as test_router

router = APIRouter()

#router.include_router(food_router)
router.include_router(nutrient_router)
router.include_router(test_router)


