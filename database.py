import aiosqlite

DB_NAME = "movies.db"


async def create_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE,
            file_id TEXT
        )
        """)
        await db.commit()


async def add_movie(code, file_id):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR REPLACE INTO movies (code, file_id) VALUES (?, ?)",
            (code, file_id)
        )
        await db.commit()


async def get_movie(code):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT file_id FROM movies WHERE code=?",
            (code,)
        )
        row = await cursor.fetchone()
        return row[0] if row else None
