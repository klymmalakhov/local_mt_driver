from pydantic import BaseModel


class PaymentSchema(BaseModel):
    type: str
    account: int
    amount: int
    currency: str
    invoice: int
    is_int: bool
    ps_code: str
