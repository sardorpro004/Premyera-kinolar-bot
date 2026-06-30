import aiosqlite

DB_NAME = "movies.db"

async def create_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS movies(
            code TEXT PRIMARY KEY,
            file_id TEXT NOT NULL
        )
        """)

        await db.commit()


async def add_user(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
            (user_id,)
        )
        await db.commit()


async def add_movie(code: str, file_id: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR REPLACE INTO movies(code,file_id) VALUES(?,?)",
            (code, file_id)
        )
        await db.commit()


async def get_movie(code: str):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT file_id FROM movies WHERE code=?",
            (code,)
        )
        return await cursor.fetchone()
