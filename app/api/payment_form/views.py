from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from app.api.payment_form.models import PaymentSchema

router = APIRouter()

# return the schema of requirement fields
@router.get("/payment-form", status_code=HTTP_200_OK)
async def get_payment_schema():
    return PaymentSchema.schema()
