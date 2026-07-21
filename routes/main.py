"""Primary site routes: home, about, services, products, contact."""
from flask import Blueprint, current_app, flash, redirect, render_template, url_for

from data.site_content import (
    BRANDS,
    CONTACT_DIRECTORY,
    NEWS,
    PARTNERS,
    TEAM,
    brands_by_category,
)
from forms.contact_form import ContactForm
from forms.newsletter_form import NewsletterForm
from models import db
from models.models import ContactMessage, NewsletterSubscriber

main = Blueprint("main", __name__)


def _local_brand(brand):
    item = dict(brand)
    item["local_link"] = url_for("main.brand_detail", slug=brand["slug"])
    return item


def _local_brands(brand_list):
    return [_local_brand(brand) for brand in brand_list]


@main.route("/")
def index():
    """Render the homepage with hero, stats, services, brands, CTA."""
    newsletter_form = NewsletterForm()
    return render_template("index.html", newsletter_form=newsletter_form, brands=_local_brands(BRANDS[:14]))


GALLERY_IMAGES = [
    "equipment-01.jpg", "equipment-02.png", "equipment-03.jpg", "equipment-04.png",
    "equipment-05.jpg", "equipment-06.jpg", "equipment-07.png", "equipment-08.jpg",
    "equipment-09.png", "equipment-10.png", "equipment-11.png", "equipment-12.jpg",
    "equipment-13.png", "equipment-14.png", "equipment-15.jpg", "equipment-16.jpg",
    "equipment-17.png", "equipment-18.png",
]


@main.route("/about")
def about():
    """Render the Company / About page."""
    newsletter_form = NewsletterForm()
    return render_template(
        "about.html",
        newsletter_form=newsletter_form,
        team=TEAM,
        partners=PARTNERS,
        gallery_images=GALLERY_IMAGES,
    )


@main.route("/services")
def services():
    """Render the Services page."""
    newsletter_form = NewsletterForm()
    return render_template(
        "services.html",
        newsletter_form=newsletter_form,
        form=ContactForm(),
        news_items=NEWS[:4],
    )


@main.route("/products")
def products():
    """Render the Agencies / product manufacturing & packaging lines page.

    The live archive lists every brand in the category (26 of them) in
    alphabetical order, not a curated subset.
    """
    newsletter_form = NewsletterForm()
    return render_template(
        "products.html",
        newsletter_form=newsletter_form,
        brands=_local_brands(brands_by_category("manufacturing")),
    )


@main.route("/quality-control")
def quality_control():
    """Render the Quality Control agencies page."""
    newsletter_form = NewsletterForm()
    return render_template(
        "quality-control.html",
        newsletter_form=newsletter_form,
        brands=_local_brands(brands_by_category("quality")),
    )


@main.route("/supply-chain")
def supply_chain():
    """Render the Supply Chain agencies page."""
    newsletter_form = NewsletterForm()
    return render_template(
        "supply-chain.html",
        newsletter_form=newsletter_form,
        brands=_local_brands(brands_by_category("supply")),
    )


@main.route("/brand/<slug>")
def brand_detail(slug):
    newsletter_form = NewsletterForm()
    brand = next((brand for brand in BRANDS if brand["slug"] == slug), None)
    if brand is None:
        return redirect(url_for("main.products"))
    related = _local_brands([item for item in BRANDS if item["slug"] != slug][:6])
    return render_template(
        "brand_detail.html",
        newsletter_form=newsletter_form,
        brand=_local_brand(brand),
        related_brands=related,
    )


@main.route("/news")
def news():
    """Render the News listing page."""
    newsletter_form = NewsletterForm()
    return render_template("news.html", newsletter_form=newsletter_form, news_items=NEWS)


@main.route("/contact", methods=["GET", "POST"])
def contact():
    """Render the contact page and process contact form submissions."""
    form = ContactForm()
    newsletter_form = NewsletterForm()

    if form.validate_on_submit():
        try:
            message = ContactMessage(
                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data,
                subject=form.subject.data,
                message=form.message.data,
            )
            db.session.add(message)
            db.session.commit()
            flash("Message sent successfully! We will get back to you soon.", "success")
        except Exception as exc:  # noqa: BLE001
            db.session.rollback()
            current_app.logger.error("Failed to save contact message: %s", exc)
            flash("Something went wrong while sending your message.", "danger")
        return redirect(url_for("main.contact"))

    if form.errors:
        flash("Please correct the errors below and try again.", "danger")

    return render_template(
        "contact.html",
        form=form,
        newsletter_form=newsletter_form,
        directory=CONTACT_DIRECTORY,
    )


@main.route("/newsletter", methods=["POST"])
def newsletter():
    """Handle newsletter subscription submissions from the footer form."""
    form = NewsletterForm()
    if form.validate_on_submit():
        existing = NewsletterSubscriber.query.filter_by(email=form.email.data).first()
        if not existing:
            db.session.add(NewsletterSubscriber(email=form.email.data))
            db.session.commit()
        flash("Thanks for subscribing to our newsletter!", "success")
    else:
        flash("Please enter a valid email address.", "danger")
    return redirect(url_for("main.index"))
