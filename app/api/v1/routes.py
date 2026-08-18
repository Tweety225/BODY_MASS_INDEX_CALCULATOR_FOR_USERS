from fastapi import APIRouter
from . import bmi as bmi_router
from . import health as health_router

router = APIRouter(prefix="/api/v1")

router.include_router(bmi_router.router, prefix="/bmi", tags=["bmi"])
router.include_router(health_router.router, prefix="/healthz", tags=["health"])
