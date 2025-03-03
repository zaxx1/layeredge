import asyncio
from random import randint
from fake_useragent import UserAgent

from core.reqs import send_prof, submit_prof, submit_light_node, submit_free_pass, submit_og_pass
from utils.file_utils import read_proxies, read_wallets_to_complete_tasks
from utils.private_key_to_wallet import private_key_to_wallet
from utils.file_utils import write_failed_tasks, write_success_tasks
from utils.log_utils import logger
from core.account import Account
from core import db
from configs import config

PRIVATE_KEYS_TO_COMPLETE_TASKS = read_wallets_to_complete_tasks()
PROXIES = read_proxies()
ua_faker = UserAgent()
write_failed_tasks('------------------------------------------------')
write_success_tasks('------------------------------------------------')

async def complete_tasks(private_key: str, proxy):
    ua = await db.get_ua(private_key_to_wallet(private_key))

    if not ua:
        ua = ua_faker.random
        await db.add_account(private_key_to_wallet(private_key), ua)

    account = Account(private_key, ua)
    logger.success(f"{account.wallet_address} | Start running tasks..")
    await asyncio.sleep(randint(config.MIN_DELAY_BEFORE_START, config.MAX_DELAY_BEFORE_START))

    if config.DO_PROOF:
        await send_prof(account, proxy)
        await asyncio.sleep(20, 30)
    if config.DO_SUBMIT_PROOF_TASK:
        await submit_prof(account, proxy)
        await asyncio.sleep(10, 30)
    if config.DO_LIGHT_NODE_RUN_TASK:
        await submit_light_node(account, proxy)
        await asyncio.sleep(10, 30)
    if config.DO_PLEDGE_PASS_HOLD_TASK:
        await submit_free_pass(account, proxy)
        await asyncio.sleep(10, 30)
    if config.DO_OG_PLEDGE_PASS_HOLD_TASK:
        await submit_og_pass(account, proxy)
        await asyncio.sleep(10, 30)

async def start():
    await db.create_database()
    tasks = []
    for private_key, proxy in zip(PRIVATE_KEYS_TO_COMPLETE_TASKS, PROXIES):
        task = asyncio.create_task(complete_tasks(private_key, proxy))
        tasks.append(task)
        await asyncio.sleep(0.1)

    while tasks:
        tasks = [task for task in tasks if not task.done()]
        await asyncio.sleep(10)

    logger.success(f"All accounts processed!")

if __name__ == '__main__':
    asyncio.run(start())