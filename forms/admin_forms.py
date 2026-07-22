"""Forms used by the /admin News management area."""
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileSize
from wtforms import PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, Optional, URL


class AdminSetupForm(FlaskForm):
    """One-time form to create the single admin account."""

    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=128)])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password", message="Passwords must match.")],
    )


class AdminLoginForm(FlaskForm):
    """Login form shown at /admin once an account exists."""

    username = StringField("Username", validators=[DataRequired(), Length(max=80)])
    password = PasswordField("Password", validators=[DataRequired()])


class DeleteForm(FlaskForm):
    """Empty form used purely to carry a CSRF token on delete buttons."""


class NewsPostForm(FlaskForm):
    """Add / edit form for a single News post.

    The image can come from either an uploaded file (image_file, saved to
    disk under static/images/news/) or a plain URL (img). If both are
    given, the uploaded file wins.
    """

    title = StringField("Title", validators=[DataRequired(), Length(max=200)])
    excerpt = TextAreaField("Excerpt", validators=[Optional(), Length(max=1000)])
    image_file = FileField(
        "Upload Image",
        validators=[
            Optional(),
            FileAllowed(["png", "jpg", "jpeg", "gif", "webp"], "Images only (png, jpg, jpeg, gif, webp)."),
            FileSize(max_size=8 * 1024 * 1024, message="Image must be under 8 MB."),
        ],
    )
    img = StringField("Or Image URL", validators=[Optional(), URL(), Length(max=500)])
    link = StringField("Read More Link", validators=[Optional(), URL(), Length(max=500)])
