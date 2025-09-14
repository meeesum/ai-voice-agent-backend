# app/db/init_db.py
from app.db.session import DBSession

TABLES = {
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """,
    "sessions": """
        CREATE TABLE IF NOT EXISTS sessions (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            started_at TIMESTAMP DEFAULT NOW(),
            ended_at TIMESTAMP
        );
    """,
    "calls": """
        CREATE TABLE IF NOT EXISTS calls (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            driver_name TEXT NOT NULL,
            driver_phone TEXT NOT NULL,
            load_number TEXT NOT NULL,
            outcome TEXT,
            transcript JSONB,
            summary JSONB,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """
}

def create_tables():
    with DBSession() as cur:
        for table_name, ddl in TABLES.items():
            cur.execute(ddl)
            print(f"✅ {table_name} table ensured.")
        cur.connection.commit()


if __name__ == "__main__":
    create_tables()
