import requests

from app.mt.models import Account, Transaction
from app.settings import MT_SERVER_URL, MT_SERVER_CERT


async def make_withdrawal_for_specific_account(account, trx: Transaction):
    uri = f"{MT_SERVER_URL}/api/accounts/{account}/withdrawal/"
    body = trx.json()
    return requests.post(
        uri,
        verify=False,
        cert=MT_SERVER_CERT,
        data=body,
        headers={'content-type': 'application/json'}
    ).json()


async def make_deposit_for_specific_account(account, trx: Transaction):
    uri = f"{MT_SERVER_URL}/api/accounts/{account}/deposit/"
    body = trx.json()
    return requests.post(
        uri,
        verify=False,
        cert=MT_SERVER_CERT,
        data=body,
        headers={'content-type': 'application/json'}
    ).json()


async def create_new_account(account: Account):
    uri = f"{MT_SERVER_URL}/api/accounts/"
    body = account.json()
    return requests.post(
        uri,
        verify=False,
        cert=MT_SERVER_CERT,
        data=body,
        headers={'content-type': 'application/json'}
    ).json()


async def get_account_data(account):
    uri = f"{MT_SERVER_URL}/api/accounts/{account}/"
    return requests.get(
        uri,
        verify=False,
        cert=MT_SERVER_CERT
    ).json()
