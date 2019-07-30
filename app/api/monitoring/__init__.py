from fastapi import APIRouter

from . import views

# route blocks of requests for monitoring
router = APIRouter()
router.include_router(
    views.router,
    tags=["monitoring"],
    responses={404: {"description": "Not found"}}
)
