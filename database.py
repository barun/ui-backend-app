import logging
import os
import psycopg2
import psycopg2.sql as sql
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS images (
            id SERIAL PRIMARY KEY,
            image_data BYTEA NOT NULL
                   )
    """)
    connection.commit()
    connection.close()

def insert_name(name):
    """Insert a name into the database."""
    connection = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = connection.cursor()
    logging.info(f"inserting user {name} into database")
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
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
def save_image_to_db(binary_data):
    """Save an image file to the PostgreSQL database."""
    try:
        # Connect to the database
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        cur = conn.cursor()

        # Insert the binary data into the table
        query = sql.SQL("INSERT INTO images (image_data) VALUES ( %s)")
        cur.execute(query, (binary_data))
        
        conn.commit()
        print(f"Image saved to the database successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()