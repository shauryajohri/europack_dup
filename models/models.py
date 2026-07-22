"""SQLAlchemy models for the Europack site.

All fields are kept nullable-friendly since this is demo/placeholder
data intended to make the site runnable out of the box.
"""
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from models import db


class Service(db.Model):
    """A service offered by Europack (Design, Support, Maintenance...)."""

    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(4), nullable=True)
    title = db.Column(db.String(120), nullable=True)
    description = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(120), nullable=True)


class StatCounter(db.Model):
    """A single "X+ Something" statistic shown in the About section."""

    __tablename__ = "stat_counters"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=True)
    suffix = db.Column(db.String(10), nullable=True, default="+")
    label = db.Column(db.String(120), nullable=True)


class BrandPartner(db.Model):
    """A manufacturing brand/partner shown in the logo carousel."""

    __tablename__ = "brand_partners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    logo = db.Column(db.String(200), nullable=True)


class Testimonial(db.Model):
    """A quote from a company representative (e.g. the CEO)."""

    __tablename__ = "testimonials"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(120), nullable=True)
    role = db.Column(db.String(120), nullable=True)
    quote = db.Column(db.Text, nullable=True)
    photo = db.Column(db.String(200), nullable=True)


class ContactMessage(db.Model):
    """A message submitted through the public contact form."""

    __tablename__ = "contact_messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(40), nullable=True)
    subject = db.Column(db.String(200), nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class NewsletterSubscriber(db.Model):
    """An email address collected from the footer newsletter form."""

    __tablename__ = "newsletter_subscribers"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class NewsPost(db.Model):
    """A News section entry, manageable from the /admin dashboard."""

    __tablename__ = "news_posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    excerpt = db.Column(db.Text, nullable=True)
    img = db.Column(db.String(500), nullable=True)
    link = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "title": self.title,
            "excerpt": self.excerpt,
            "img": self.img,
            "link": self.link,
        }


class AdminUser(db.Model):
    """The single admin account used to manage the News section.

    Only one admin account can exist at a time: visiting /admin before
    any account has been created shows a one-time setup form instead
    of the login form.
    """

    __tablename__ = "admin_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
