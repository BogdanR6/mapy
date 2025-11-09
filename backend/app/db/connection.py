import sqlite3
from app.core.config import DATABASE_PATH

def get_connection():
    # relative to container working dir
    conn = sqlite3.connect(DATABASE_PATH)

    # enable dict-like access
    conn.row_factory = sqlite3.Row

    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    _ = cur.execute("""
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT UNIQUE,
            name TEXT,
            lat REAL,
            lon REAL
        )
    """)
    conn.commit()
    conn.close()
