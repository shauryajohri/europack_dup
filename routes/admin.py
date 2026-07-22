"""Admin area: /admin login + News section content management.

Auth model: a single admin account. The first time anyone visits
/admin and no account exists yet, they're shown a one-time setup
form to create it. After that, /admin always shows the login form
until a valid session cookie is present.
"""
import os
import uuid
from functools import wraps

from flask import Blueprint, current_app, flash, redirect, render_template, session, url_for
from werkzeug.utils import secure_filename

from forms.admin_forms import AdminLoginForm, AdminSetupForm, DeleteForm, NewsPostForm
from models import db
from models.models import AdminUser, NewsPost

admin = Blueprint("admin", __name__, url_prefix="/admin")


def _save_uploaded_image(file_storage):
    """Save an uploaded news image to disk and return its /static URL path.

    Returns None if no file was actually submitted.
    """
    if not file_storage or not file_storage.filename:
        return None

    upload_folder = current_app.config["NEWS_UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)

    original_name = secure_filename(file_storage.filename)
    ext = original_name.rsplit(".", 1)[-1].lower() if "." in original_name else ""
    unique_name = f"{uuid.uuid4().hex}.{ext}" if ext else uuid.uuid4().hex
    file_storage.save(os.path.join(upload_folder, unique_name))

    url_path = current_app.config["NEWS_UPLOAD_URL_PATH"]
    return f"{url_path}/{unique_name}"


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("admin_id"):
            return redirect(url_for("admin.login"))
        return view(*args, **kwargs)

    return wrapped


@admin.route("/", methods=["GET", "POST"])
def login():
    """Entry point for /admin.

    Shows the one-time setup form if no admin account exists yet,
    otherwise shows the login form. Already-logged-in visitors are
    sent straight to the dashboard.
    """
    if session.get("admin_id"):
        return redirect(url_for("admin.dashboard"))

    if AdminUser.query.first() is None:
        return redirect(url_for("admin.setup"))

    form = AdminLoginForm()
    if form.validate_on_submit():
        user = AdminUser.query.filter_by(username=form.username.data.strip()).first()
        if user and user.check_password(form.password.data):
            session.clear()
            session["admin_id"] = user.id
            session.permanent = True
            flash("Welcome back!", "success")
            return redirect(url_for("admin.dashboard"))
        flash("Invalid username or password.", "danger")

    return render_template("admin/login.html", form=form)


@admin.route("/setup", methods=["GET", "POST"])
def setup():
    """One-time creation of the single admin account."""
    if AdminUser.query.first() is not None:
        return redirect(url_for("admin.login"))

    form = AdminSetupForm()
    if form.validate_on_submit():
        user = AdminUser(username=form.username.data.strip())
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        session.clear()
        session["admin_id"] = user.id
        session.permanent = True
        flash("Admin account created. You're logged in.", "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("admin/setup.html", form=form)


@admin.route("/logout")
def logout():
    session.clear()
    flash("Logged out.", "success")
    return redirect(url_for("admin.login"))


@admin.route("/dashboard")
@login_required
def dashboard():
    posts = NewsPost.query.order_by(NewsPost.created_at.desc()).all()
    return render_template("admin/dashboard.html", posts=posts, delete_form=DeleteForm())


@admin.route("/news/new", methods=["GET", "POST"])
@login_required
def news_new():
    form = NewsPostForm()
    if form.validate_on_submit():
        uploaded_path = _save_uploaded_image(form.image_file.data)
        post = NewsPost(
            title=form.title.data.strip(),
            excerpt=form.excerpt.data,
            img=uploaded_path or form.img.data,
            link=form.link.data,
        )
        db.session.add(post)
        db.session.commit()
        flash("News post added.", "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/news_form.html", form=form, mode="new")


@admin.route("/news/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def news_edit(post_id):
    post = NewsPost.query.get_or_404(post_id)
    form = NewsPostForm(obj=post)
    if form.validate_on_submit():
        uploaded_path = _save_uploaded_image(form.image_file.data)
        post.title = form.title.data.strip()
        post.excerpt = form.excerpt.data
        post.img = uploaded_path or form.img.data
        post.link = form.link.data
        db.session.commit()
        flash("News post updated.", "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/news_form.html", form=form, mode="edit", post=post)


@admin.route("/news/<int:post_id>/delete", methods=["POST"])
@login_required
def news_delete(post_id):
    form = DeleteForm()
    post = NewsPost.query.get_or_404(post_id)
    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()
        flash("News post removed.", "success")
    else:
        flash("Could not delete that post. Please try again.", "danger")
    return redirect(url_for("admin.dashboard"))
