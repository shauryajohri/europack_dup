"""One-off script: copy news posts + the admin account from the old
europack.db (SQLite) into the new MySQL 'europack' database.

Safe to run more than once — it skips posts/usernames that already
exist in MySQL instead of duplicating them.

Usage (from the europack_flask folder, with your venv activated):

    python scripts/migrate_sqlite_to_mysql.py

Requires:
  - The old SQLite file at europack.db (created by earlier runs of the app).
  - MySQL running in XAMPP with the 'europack' database already created.
  - config.py / DATABASE_URL already pointing at MySQL (this is the default
    after the switch-over, so you normally don't need to set anything).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text  # noqa: E402

from app import create_app  # noqa: E402
from models import db  # noqa: E402
from models.models import AdminUser, NewsPost  # noqa: E402

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLITE_PATH = os.path.join(BASE_DIR, "europack.db")


def main():
    if not os.path.exists(SQLITE_PATH):
        print(f"No old SQLite database found at {SQLITE_PATH} — nothing to migrate.")
        return

    sqlite_engine = create_engine(f"sqlite:///{SQLITE_PATH}")

    app = create_app("development")  # uses MySQL per config.py / DATABASE_URL
    with app.app_context():
        with sqlite_engine.connect() as conn:
            # --- news_posts ---
            try:
                rows = conn.execute(text(
                    "SELECT title, excerpt, img, link FROM news_posts"
                )).fetchall()
            except Exception as exc:  # noqa: BLE001
                print(f"Could not read news_posts from the old SQLite file: {exc}")
                rows = []

            existing_titles = {p.title for p in NewsPost.query.all()}
            added = 0
            for row in rows:
                title = row[0]
                if title in existing_titles:
                    continue
                db.session.add(NewsPost(
                    title=title, excerpt=row[1], img=row[2], link=row[3],
                ))
                added += 1
            db.session.commit()
            print(f"Migrated {added} news post(s) into MySQL.")

            # --- admin_users ---
            try:
                admin_rows = conn.execute(text(
                    "SELECT username, password_hash FROM admin_users"
                )).fetchall()
            except Exception as exc:  # noqa: BLE001
                print(f"Could not read admin_users from the old SQLite file: {exc}")
                admin_rows = []

            existing_usernames = {u.username for u in AdminUser.query.all()}
            admin_added = 0
            for row in admin_rows:
                username = row[0]
                if username in existing_usernames:
                    continue
                user = AdminUser(username=username, password_hash=row[1])
                db.session.add(user)
                admin_added += 1
            db.session.commit()
            if admin_added:
                print(f"Migrated {admin_added} admin account(s) into MySQL "
                      "(same username/password as before).")
            else:
                print("No new admin accounts to migrate (already present, or none found).")


if __name__ == "__main__":
    main()
