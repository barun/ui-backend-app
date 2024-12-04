import sqlite3

DB_NAME = "data.db"

def init_db():
    """Initialize the database and create the table if it doesn't exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def insert_name(name):
    """Insert a name into the database."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    connection.commit()
    connection.close()

def get_all_names():
    """Retrieve all names from the database."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    connection.close()
    return rows
