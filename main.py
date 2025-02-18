import asyncio

from utils.Console import Console
from configs import config
from core import get_refs
from core import register
from core import farm
from core import db


async def main():
  Console().build()
  await db.create_database()
  tasks = []

  if config.GET_REFF_CODES:
    tasks.append(asyncio.create_task(get_refs.start()))

  if config.REGISTER_MODE:
    tasks.append(asyncio.create_task(register.start()))

  if config.FARM_MODE:
    tasks.append(asyncio.create_task(farm.start()))

  if tasks:
    await asyncio.gather(*tasks)


asyncio.run(main())
