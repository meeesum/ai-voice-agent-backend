import getpass
import bcrypt
from app.db.session import DBSession

def create_superuser():
    print("🚀 Create Superuser")
    email = input("Enter email: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    # hash password
    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    with DBSession() as cur:
        cur.execute("SELECT id FROM users WHERE email = %s;", (email,))
        existing = cur.fetchone()
        if existing:
            print("❌ User already exists.")
            return

        cur.execute(
            """
            INSERT INTO users (email, password)
            VALUES (%s, %s)
            RETURNING id;
            """,
            (email, hashed_pw)
        )
        new_user = cur.fetchone()
        print(f"✅ Superuser created with ID: {new_user['id']}")

if __name__ == "__main__":
    create_superuser()
