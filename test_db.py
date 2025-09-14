import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("✅ Connected to Supabase DB successfully!")
        return conn
    except Exception as e:
        print("❌ Failed to connect:", e)
        return None

# Example usage
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT NOW();")
        print(cur.fetchone())
        cur.close()
        conn.close()
