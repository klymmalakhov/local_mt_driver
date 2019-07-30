from fastapi import APIRouter

from . import views

# route blocks of requests for communication with invoice
router = APIRouter()
router.include_router(
    views.router,
    prefix="/invoice",
    tags=["invoice"],
    responses={404: {"description": "Not found"}}
)