import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    """
    Get a new database connection to Supabase using psycopg2.
    Returns a connection object or None if failed.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST").strip(),
            port=int(os.getenv("DB_PORT")),
            dbname=os.getenv("DB_NAME").strip(),
            user=os.getenv("DB_USER").strip(),
            password=os.getenv("DB_PASSWORD").strip(),
            sslmode=os.getenv("DB_SSLMODE", "require")  # default to require
        )
        return conn
    except Exception as e:
        print("❌ Failed to connect:", e)
        return None


class DBSession:
    """
    Context manager for a DB session.
    Usage:
        with DBSession() as cur:
            cur.execute("SELECT * FROM users;")
            results = cur.fetchall()
    """
    def __enter__(self):
        self.conn = get_db_connection()
        if not self.conn:
            raise ConnectionError("Cannot connect to the database")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.cur.close()
            self.conn.close()
