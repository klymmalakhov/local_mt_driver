from fastapi import APIRouter

from . import views

# route blocks of requests for communication with payment form
router = APIRouter()
router.include_router(
    views.router,
    tags=["payment form"],
    responses={404: {"description": "Not found"}}
)