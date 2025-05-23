import asyncio
import aiosqlite

DB_PATH = 'users.db'

async def async_fetch_users():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            return users

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            users = await cursor.fetchall()
            return users

async def fetch_concurrently():
    all_users_task = async_fetch_users()
    older_users_task = async_fetch_older_users()

    all_users, older_users = await asyncio.gather(all_users_task, older_users_task)

    print("All users:")
    for user in all_users:
        print(user)
    print("\nUsers older than 40:")
    for user in older_users:
        print(user)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
