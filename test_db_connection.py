import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Retrieve database URL from environment variables
DATABASE_URL = os.environ.get('DATABASE_URL', 'mysql+pymysql://user:password@localhost/engine_swap')

def test_db_connection():
    """Test database connectivity and perform a simple query to fetch the MySQL version."""
    try:
        engine = create_engine(DATABASE_URL)
        # Connect to the database
        with engine.connect() as connection:
            result = connection.execute("SELECT VERSION();")
            version = result.fetchone()
            print(f"Successfully connected to MySQL database. Version: {version[0]}")
    except SQLAlchemyError as e:
        print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    test_db_connection()
