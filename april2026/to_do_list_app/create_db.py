import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute(
    """CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT)"""
)

cur.execute("""
CREATE TABLE to_do_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    description TEXT,
    completed BOOLEAN DEFAULT 0
)
""")

conn.commit()
conn.close()