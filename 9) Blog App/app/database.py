# need to run following command for password salting
# pip install flask-bcrypt

import sqlite3
from pathlib import Path
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "app/blogDb.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

 
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create User Table
    # AUTOINCREMENT" will automatically create the "sqlite_sequence" table in Db to track record
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role INTEGER NOT NULL DEFAULT 2,
            profile_path TEXT,
            is_active INTEGER DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create Blog Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            image_path TEXT,
            is_active INTEGER DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

    # Seed Admin User
    seed_admin()

def seed_admin():
    """Seed an admin user if no users exist."""
    conn = get_db_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    if count == 0:
        hashed_password = bcrypt.generate_password_hash("123").decode('utf-8')
        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            ("Waqas Ahmed", "waqaxahmed786@gmail.com", hashed_password, 1)
        )
        conn.commit()

    conn.close()
