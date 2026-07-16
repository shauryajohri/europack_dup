"""Application factory for the Europack Flask website."""
import os

from flask import Flask, render_template, send_from_directory

from config import config_by_name
from forms.newsletter_form import NewsletterForm
from models import db, init_db


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

    init_db(app)

    from routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.static_folder, "icons"),
            "favicon-32.png",
            mimetype="image/png",
        )

    register_error_handlers(app)

    # Dev convenience: create tables if they do not exist yet.
    with app.app_context():
        try:
            db.create_all()
        except Exception:  # noqa: BLE001
            pass

    return app


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
