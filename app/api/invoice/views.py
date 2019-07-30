import requests
from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from app.api.payment_form.models import PaymentSchema
from app.db.initialization import events, database
from app.settings import MT_SERVER_URL, MT_SERVER_CERT, ERROR_NOT_IMPLEMENTED, ERROR_WRONG_TYPE

router = APIRouter()


@router.post("/", status_code=HTTP_201_CREATED)
async def create_invoice(trx: PaymentSchema):
    if ((trx.type != "withdrawal") & (trx.type != "deposit")):
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content=ERROR_WRONG_TYPE)
    if trx.type == "withdrawal":
        trx.amount = trx.amount * -1

    account = trx.account
    type_trx = trx.type
    body = trx.json()
    uri = f"{MT_SERVER_URL}/api/accounts/{account}/{type_trx}/"

    mt_response = requests.post(
        uri,
        verify=False,
        cert=MT_SERVER_CERT,
        data=body,
        headers={'content-type': 'application/json'}
    ).json()

    query = events.insert().values(
        id_event=trx.invoice,
        event_request=str(trx),
        event_response=str(mt_response)
    )
    await database.execute(query)

    return mt_response


@router.get("/{invoice_id}", status_code=HTTP_400_BAD_REQUEST)
async def get_invoice_by_id(invoice_id: str):
    return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content=ERROR_NOT_IMPLEMENTED)


@router.get("/{invoice_id}/events", status_code=HTTP_400_BAD_REQUEST)
async def get_events_by_invoice_id(invoice_id: str):
    return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content=ERROR_NOT_IMPLEMENTED)


@router.post("/cancel", status_code=HTTP_400_BAD_REQUEST)
async def cancel_invoice(invoice_id: str):
    return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content=ERROR_NOT_IMPLEMENTED)
