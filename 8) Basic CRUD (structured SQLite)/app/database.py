import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "app/blogDb.db"

def init_db():
    print(DB_PATH)
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    return sqlite3.connect(DB_PATH)