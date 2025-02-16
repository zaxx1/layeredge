import aiosqlite
import asyncio
from fake_useragent import UserAgent

from configs.constants import DATABASE_PATH
from utils.file_utils import read_register

# crate db
async def create_database():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                wallet_address TEXT NOT NULL UNIQUE,
                user_agent TEXT NOT NULL,
                points INTEGER NOT NULL
            )
        """)
        await db.commit()

async def add_account(wallet_address: str, user_agent: str, points: int = 0):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("INSERT INTO accounts (wallet_address, user_agent, points) VALUES (?, ?, ?)",
                         (wallet_address, user_agent, points))
        await db.commit()

# get all accounts
async def get_accounts():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute("SELECT id, wallet_address, user_agent, points FROM accounts") as cursor:
            return await cursor.fetchall()

async def get_ua(wallet_address: str):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute("SELECT user_agent FROM accounts WHERE wallet_address = ?", (wallet_address,)) as cursor:
            res = await cursor.fetchall()
            if len(res):
                return res[0][0]
            else:
                return None

async def get_total_points():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute("SELECT sum(points) FROM accounts") as cursor:
            return await cursor.fetchone()

async def is_address_in_db(wallet_address: str) -> bool:
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute("SELECT 1 FROM accounts WHERE wallet_address = ?", (wallet_address,)) as cursor:
            return await cursor.fetchone() is not None

async def add_wallets_from_register():
    private_keys = read_register()
    ua = UserAgent(os=["Windows", "Linux", "Ubuntu", "Mac OS X"])

    for private_key in private_keys:
        if not await is_address_in_db(private_key):
            await add_account(private_key, ua.random, 0)

async def update_points(wallet_address: str, new_points: int):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("UPDATE accounts SET points = ? WHERE wallet_address = ?", (new_points, wallet_address))
        await db.commit()
