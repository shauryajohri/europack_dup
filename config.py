"""Application configuration classes."""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration shared across environments."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

    # Uses XAMPP's bundled MySQL/MariaDB by default: root user, no password,
    # localhost:3306, database name "europack". Create that database once in
    # phpMyAdmin (or run `CREATE DATABASE europack;` in the MySQL console) —
    # Flask-SQLAlchemy will create the tables inside it automatically.
    # Override with a DATABASE_URL env var to point elsewhere (e.g. back to
    # SQLite for quick local testing: sqlite:///europack.db).
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost:3306/europack?charset=utf8mb4",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True

    # Where uploaded news/blog images are saved (served from /static/...).
    NEWS_UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "images", "news")
    NEWS_UPLOAD_URL_PATH = "images/news"
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 8 MB upload cap

    SITE_NAME = "Europack"
    SITE_TAGLINE = "Supporting the Manufacturing Industry Since 1972"
    CONTACT_EMAIL = "info@europack.gr"
    CONTACT_PHONE = "+30 210 9607102-3"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    # Ready to swap in PostgreSQL:
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
