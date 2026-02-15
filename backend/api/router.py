from fastapi import APIRouter

from modules.test.router import router as test_router

router = APIRouter()

router.include_router(test_router)

