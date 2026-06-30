import sqlite3

db = sqlite3.connect("movies.db")
sql = db.cursor()

def create_db():
    sql.execute("""
    CREATE TABLE IF NOT EXISTS movies(
        code TEXT PRIMARY KEY,
        file_id TEXT
    )
    """)
    db.commit()

def add_movie(code, file_id):
    sql.execute(
        "INSERT OR REPLACE INTO movies(code, file_id) VALUES(?, ?)",
        (code, file_id)
    )
    db.commit()

def get_movie(code):
    sql.execute(
        "SELECT file_id FROM movies WHERE code=?",
        (code,)
    )
    return sql.fetchone()
