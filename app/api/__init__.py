from fastapi import APIRouter

from . import invoice, monitoring, payment_form

router = APIRouter()
router.include_router(invoice.router)
router.include_router(monitoring.router)
router.include_router(payment_form.router)
