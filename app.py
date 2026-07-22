"""Application factory for the Europack Flask website."""
import os

from flask import Flask, render_template, send_from_directory, url_for

from config import config_by_name
from forms.newsletter_form import NewsletterForm
from models import db, init_db


def news_image_url(img):
    """Resolve a NewsPost.img value to a usable <img src>.

    img is either a full external URL (http/https, from the "Image URL"
    field) or a path relative to /static (from an uploaded file, e.g.
    "images/news/<uuid>.jpg"). Falls back to a placeholder if empty.
    """
    if not img:
        return url_for("static", filename="images/site/og-image.png")
    if img.startswith("http://") or img.startswith("https://"):
        return img
    return url_for("static", filename=img)


def create_app(config_name=None):
    """Create and configure the Flask application instance.

    Args:
        config_name: One of "development", "production", "default".
            Falls back to the FLASK_ENV environment variable, then
            to "default".
    """
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "default")

    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name, config_by_name["default"]))
    app.jinja_env.globals["news_image_url"] = news_image_url

    init_db(app)

    from routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from routes.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.static_folder, "icons"),
            "favicon-32.png",
            mimetype="image/png",
        )

    register_error_handlers(app)

    # Dev convenience: create tables if they do not exist yet, and seed
    # the News section from the static placeholder data the first time
    # the app runs (so the admin-managed table doesn't start empty).
    with app.app_context():
        try:
            db.create_all()
            _seed_news_if_empty()
        except Exception as exc:  # noqa: BLE001
            app.logger.error(
                "Could not connect/initialize the database (%s). "
                "If you're using MySQL via XAMPP, make sure MySQL is running "
                "in the XAMPP Control Panel and that the 'europack' database "
                "exists (create it once in phpMyAdmin). Error: %s",
                app.config.get("SQLALCHEMY_DATABASE_URI"),
                exc,
            )

    return app


def _seed_news_if_empty():
    """Populate the news_posts table from data/site_content.py once.

    Runs only when the table has never been written to, so it never
    overwrites posts added or edited from the admin dashboard.
    """
    from data.site_content import NEWS
    from models.models import NewsPost

    if NewsPost.query.first() is not None:
        return

    for item in NEWS:
        db.session.add(
            NewsPost(
                title=item.get("title", ""),
                excerpt=item.get("excerpt"),
                img=item.get("img"),
                link=item.get("link"),
            )
        )
    db.session.commit()


def register_error_handlers(app):
    """Attach custom 404 / 500 error pages to the app."""

    @app.errorhandler(404)
    def not_found(error):  # noqa: ANN001
        newsletter_form = NewsletterForm()
        return render_template("errors/404.html", newsletter_form=newsletter_form), 404

    @app.errorhandler(500)
    def server_error(error):  # noqa: ANN001
        newsletter_form = NewsletterForm()
        return render_template("errors/500.html", newsletter_form=newsletter_form), 500


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
