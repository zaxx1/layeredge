import asyncio

from utils.Console import Console
from configs import config
from core import register
from core import farm


async def main():
  Console().build()
  tasks = []

  if config.REGISTER_MODE:
    tasks.append(asyncio.create_task(register.start()))

  if config.FARM_MODE:
    tasks.append(asyncio.create_task(farm.start()))

  if tasks:
    await asyncio.gather(*tasks)


asyncio.run(main())
