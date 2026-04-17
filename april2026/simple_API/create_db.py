import sqlite3
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "expenses.db")

def get_db():
    return sqlite3.connect(db_path)

def init_db():

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              amount REAL)
    """)

    conn.commit()
    conn.close()

init_db()