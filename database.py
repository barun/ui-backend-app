import logging
import os
import psycopg2

# Get the DATABASE_URL from Render's environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

def init_db():
    """Initialize the database and create the table if it doesn't exist."""
    connection = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
                   )
    """)
    connection.commit()
    connection.close()

def insert_name(name):
    """Insert a name into the database."""
    connection = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = connection.cursor()
    logging.info(f"inserting user {name} into database")
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    connection.commit()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    logging.info(f"Retrieved after insert {len(rows)} users from database")
    connection.close()

def get_all_names():
    """Retrieve all names from the database."""
    logging.info("Fetching all users from database")
    connection = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        logging.info(f"Retrieved {len(rows)} users from database")
        return rows
    except Exception as e:
        logging.error(f"Error fetching users: {str(e)}")
        raise
    finally:
        connection.close()
