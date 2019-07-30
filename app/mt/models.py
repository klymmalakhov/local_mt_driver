from pydantic import BaseModel
from pydantic import UUID4


class Account(BaseModel):
    server_code: str
    account_type: str
    user_uid: UUID4
    name: str
    currency: str
    email: str
    partner_account: int
    leverage: int
    terminal_password: str
    investor_password: str
    is_swap_free: bool
    read_only: bool


class Transaction(BaseModel):
    amount: int
    currency: str
    invoice: int
    is_int: bool
    ps_code: str
