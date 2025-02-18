import asyncio
from random import randint

from core.reqs import get_ref_code
from utils.file_utils import read_proxies, read_wallets_to_get_refs, write_ref_codes, write_failed_account
from utils.private_key_to_wallet import private_key_to_wallet
from utils.log_utils import logger
from core.account import Account
from core import db
from fake_useragent import UserAgent

PRIVATE_KEYS_TO_GET_REFS = read_wallets_to_get_refs()
PROXIES = read_proxies()

async def get_referral_code(private_key: str, proxy):
    ua = await db.get_ua(private_key_to_wallet(private_key))

    ua_faker = UserAgent()
    if not ua:
        ua = ua_faker.random

    account = Account(private_key, ua)
    logger.success(f"{account.wallet_address} | Starting to get referral codes..")
    await asyncio.sleep(randint(0, 60))

    ref_code = await get_ref_code(account, proxy)

    if ref_code:
        write_ref_codes(ref_code)
        logger.success(f"{account.wallet_address} | Successfully got referral code, check results/accounts_refs.txt")
    else:
        write_failed_account(private_key)
        logger.error(f"{private_key} | Error while receiving referral code!")


async def start():
    tasks = []
    for private_key, proxy in zip(PRIVATE_KEYS_TO_GET_REFS, PROXIES):
        tasks.append(asyncio.create_task(get_referral_code(private_key, proxy)))
    await asyncio.gather(*tasks)