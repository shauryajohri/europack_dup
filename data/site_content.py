"""Real content sourced from the live europack.gr site: represented brands,
team members, news articles, and contact directory. Brand and site images are
served locally from static/images/ (downloaded from the client's own
WordPress media library at europack.gr/wp-content/uploads/...).
"""

BRANDS = [
    {"name": "All-Fill", "slug": "all-fill", "img": "/static/images/brands/all-fill.webp", "link": "https://europack.gr/en/antiprosopeia/all-fill/", "categories": ["food", "manufacturing"]},
    {"name": "AluSense", "slug": "alu-sense", "img": "/static/images/brands/alu-sense.png", "link": "https://europack.gr/en/antiprosopeia/alu-sense/", "categories": ["manufacturing", "coffee"]},
    {"name": "CEIA", "slug": "ceia", "img": "/static/images/brands/ceia.jpg", "link": "https://europack.gr/en/antiprosopeia/ceia/", "categories": ["food", "manufacturing", "quality"]},
    {"name": "CEIA", "slug": "ceia-2", "img": "/static/images/brands/ceia-2.webp", "link": "https://europack.gr/en/antiprosopeia/ceia-2/", "categories": ["manufacturing", "pharma"]},
    {"name": "Claranor", "slug": "claranor", "img": "/static/images/brands/claranor.png", "link": "https://europack.gr/en/antiprosopeia/claranor/", "categories": ["food", "manufacturing", "pharma"]},
    {"name": "Colombini", "slug": "colombini", "img": "/static/images/brands/colombini.jpg", "link": "https://europack.gr/en/antiprosopeia/colombini/", "categories": ["manufacturing", "coffee"]},
    {"name": "Detectamet", "slug": "detectamet", "img": "/static/images/brands/detectamet.png", "link": "https://europack.gr/en/antiprosopeia/detectamet/", "categories": ["consumables", "manufacturing"]},
    {"name": "Econocorp", "slug": "econocorp", "img": "/static/images/brands/econocorp.png", "link": "https://europack.gr/en/antiprosopeia/econocorp/", "categories": ["food", "manufacturing"]},
    {"name": "Endoline", "slug": "endoline", "img": "/static/images/brands/endoline.png", "link": "https://europack.gr/en/antiprosopeia/endoline/", "categories": ["food", "manufacturing"]},
    {"name": "Fette Compacting", "slug": "fette-compacting", "img": "/static/images/brands/fette-compacting.png", "link": "https://europack.gr/en/antiprosopeia/fette-compacting/", "categories": ["manufacturing", "pharma"]},
    {"name": "GEYSSEL", "slug": "geyssel", "img": "/static/images/brands/geyssel.jpg", "link": "https://europack.gr/en/antiprosopeia/geyssel/", "categories": ["food", "manufacturing"]},
    {"name": "Glatt Group", "slug": "glatt-group", "img": "/static/images/brands/glatt-group.jpg", "link": "https://europack.gr/en/antiprosopeia/glatt-group/", "categories": ["manufacturing", "pharma"]},
    {"name": "Heat and Control", "slug": "heat-and-control", "img": "/static/images/brands/heat-and-control.jpg", "link": "https://europack.gr/en/antiprosopeia/heat-and-control/", "categories": ["food", "manufacturing"]},
    {"name": "IMA Ilapak", "slug": "ima-ilapak", "img": "/static/images/brands/ima-ilapak.jpg", "link": "https://europack.gr/en/antiprosopeia/ima-ilapak/", "categories": ["food", "manufacturing"]},
    {"name": "Ishida", "slug": "ishida", "img": "/static/images/brands/ishida.webp", "link": "https://europack.gr/en/antiprosopeia/ishida/", "categories": ["food", "manufacturing", "quality", "pharma"]},
    {"name": "Mpac", "slug": "mpac", "img": "/static/images/brands/mpac.jpg", "link": "https://europack.gr/en/antiprosopeia/mpac/", "categories": ["food", "manufacturing"]},
    {"name": "Oli", "slug": "oli", "img": "/static/images/brands/oli.jpg", "link": "https://europack.gr/en/antiprosopeia/oli/", "categories": ["food", "manufacturing"]},
    {"name": "Packline", "slug": "packline", "img": "/static/images/brands/packline.jpg", "link": "https://europack.gr/en/antiprosopeia/packline/", "categories": ["food", "manufacturing"]},
    {"name": "Pharma Technology", "slug": "pharma-technology", "img": "/static/images/brands/pharma-technology.png", "link": "https://europack.gr/en/antiprosopeia/pharma-technology/", "categories": ["manufacturing", "pharma"]},
    {"name": "Probat", "slug": "probat", "img": "/static/images/brands/probat.png", "link": "https://europack.gr/en/antiprosopeia/probat/", "categories": ["manufacturing", "coffee"]},
    {"name": "SIG Group", "slug": "sig-group", "img": "/static/images/brands/sig-group.webp", "link": "https://europack.gr/en/antiprosopeia/sig-group/", "categories": ["food", "manufacturing"]},
    {"name": "Sollas", "slug": "sollas", "img": "/static/images/brands/sollas.png", "link": "https://europack.gr/en/antiprosopeia/sollas/", "categories": ["food", "manufacturing"]},
    {"name": "Supura", "slug": "supura", "img": "/static/images/brands/supura.png", "link": "https://europack.gr/en/antiprosopeia/supura/", "categories": ["food", "manufacturing"]},
    {"name": "Swiss Can Machinery", "slug": "swiss-can-machinery", "img": "/static/images/brands/swiss-can-machinery.jpg", "link": "https://europack.gr/en/antiprosopeia/swiss-can-machinery/", "categories": ["food", "manufacturing"]},
    {"name": "Tecma Aries", "slug": "tecma-aries", "img": "/static/images/brands/tecma-aries.webp", "link": "https://europack.gr/en/antiprosopeia/tecma-aries/", "categories": ["food", "manufacturing"]},
    {"name": "Volpak", "slug": "volpak", "img": "/static/images/brands/volpak.jpg", "link": "https://europack.gr/en/antiprosopeia/volpak/", "categories": ["food", "manufacturing"]},
    {"name": "Stommpy", "slug": "stommpy", "img": "/static/images/brands/stommpy.webp", "link": "https://europack.gr/en/antiprosopeia/stommpy/", "categories": ["supply"]},
]

_PARTNER_BASE = "https://europack.gr/wp-content/uploads/2025/07/"

# "Our Customers" logo marquee on the Company page. Images are hotlinked to the
# client's own WordPress media library so they display immediately; drop local
# copies into static/images/partners/ and switch the base later if desired.
PARTNERS = [
    {"file": "adelco.png", "link": "https://www.adelco.gr/"},
    {"file": "2.Agrifreda.png", "link": "https://agrifreda.gr/index.php?lang=en"},
    {"file": "3.AgroPhoenix.png", "link": "https://agrophoenix.gr"},
    {"file": "4.Alambra.petroubros-1.png", "link": "https://petroubros.com.cy/el/"},
    {"file": "5.Archontakis.png", "link": "https://www.archontakis.com/"},
    {"file": "6.ARIfood.png", "link": "https://arifoods.gr/company/"},
    {"file": "7.Bennett-1.png", "link": "https://bennett.gr/"},
    {"file": "8.Boehringer-Ingelheim.png", "link": "https://www.boehringer-ingelheim.com/"},
    {"file": "9.Cafetex-1.png", "link": "https://cafetex.gr/"},
    {"file": "damavand.png", "link": "https://www.damavand.gr/"},
    {"file": "11.dandalis.png", "link": "https://dandalis.gr/"},
    {"file": "12.DELTA_.png", "link": "https://www.delta.gr/"},
    {"file": "elbisco_logo.png", "link": "https://elbisco.gr/"},
    {"file": "14.Elpen_.png", "link": "https://www.elpen.gr/"},
    {"file": "15.Elvida-1.png", "link": "https://www.elvidafoods.gr/"},
    {"file": "Fage.png", "link": "https://home.fage/"},
    {"file": "FAMAR.png", "link": "https://www.famar-group.com/"},
    {"file": "18.Friesland-Campania.png", "link": "https://www.nounou.gr/"},
    {"file": "20.genepharm-1.png", "link": "https://www.genepharm.com/en"},
    {"file": "21.george-charalambous-1.png", "link": "https://gcharalambous.com/el/"},
    {"file": "22.ellinikoi-ximoi-logo-web.png", "link": "https://hellenicjuices.gr/"},
    {"file": "24.Ifantis-1.png", "link": "https://ifantis.gr/"},
    {"file": "25.jacobs-douwe-egberts-professional.png", "link": "https://www.jacobsdouweegbertsprofessional.gr/"},
    {"file": "26.kore_-1.png", "link": "https://www.kore.gr"},
    {"file": "krikri-logo-gr.png", "link": "https://www.krikri.gr/"},
    {"file": "kyknos-full-logo-gold.png", "link": "https://kyknoscanning.com/el/"},
    {"file": "29.makedoniki-logo-1.png", "link": "https://www.makedoniki.gr/"},
    {"file": "30.mandrekas-1.png", "link": "https://www.mandrekas.gr/"},
    {"file": "31.megas-yeeros.png", "link": "https://www.megasyeeros.gr/"},
    {"file": "32.mevgal-logo.png", "link": "https://mevgal.gr/"},
    {"file": "Mondelez-International.png", "link": "https://www.mondelezinternational.com/"},
    {"file": "34.neogal-1.png", "link": "https://neogal.gr/en"},
    {"file": "35.nestle-logo-gr-1-1.png", "link": "https://www.nestle.gr/"},
    {"file": "36.NIKAS_.png", "link": "https://nikas.gr/"},
    {"file": "37.OnePharma-1.png", "link": "https://www.onepharma.gr/en/"},
    {"file": "38.Ouzounoglou-1.png", "link": "https://www.ouzounoglou.gr/"},
    {"file": "39.Lavdas-1.png", "link": "https://lavdas.gr/?lang=en"},
    {"file": "40.papadopoulos.png", "link": "https://papadopoulou.gr/"},
    {"file": "41.Pellito-1.png", "link": "https://pellito.gr/"},
    {"file": "42.Pharmapath-1.png", "link": "https://www.pharmapath.eu/"},
    {"file": "43.Pharmathen-1.png", "link": "https://www.pharmathen.com/"},
    {"file": "44.pharmazac-1.png", "link": "https://pharmazac.gr/"},
    {"file": "45.QualitaUnica-1.png", "link": "https://www.qualitaunica.gr/?lang=el"},
    {"file": "46.Rafarm-1.png", "link": "https://www.rafarmgroup.gr/"},
    {"file": "47.Rontis-1.png", "link": "https://rontis.com/"},
    {"file": "48.Uni-Pharma.png", "link": "https://www.uni-pharma.gr/el/"},
    {"file": "49.Zita-dairies-1.png", "link": "https://www.zitadairies.com/en/"},
    {"file": "50.ΒΙΑΝΕΞlogo-1.png", "link": "https://www.vianex.gr/intro"},
    {"file": "51.dodoni.png", "link": "https://dodoni.com/"},
    {"file": "52.evrofarma.png", "link": "https://evrofarma.gr/"},
    {"file": "53.Ellinika-galaktokomeia.png", "link": "https://www.hellenicdairies.com/en/"},
    {"file": "54.ΙΟΝ-1.png", "link": "https://www.ion.gr/"},
    {"file": "55.ΜπαρμπαΣταθης-1.png", "link": "https://www.barbastathis.com/"},
    {"file": "56.Χαραλαμπίδης.Κριστης.png", "link": "https://www.charalambideschristis.com.cy/"},
]

for _p in PARTNERS:
    _p["img"] = _PARTNER_BASE + _p["file"]


CATEGORY_LABELS = {
    "manufacturing": "Product Manufacturing & Packaging Lines",
    "quality": "Quality Control",
    "supply": "Supply Chain",
    "food": "Food Industry",
    "coffee": "Coffee Production",
    "pharma": "Pharmaceutical Industry",
    "consumables": "Consumables",
}


# Maps our internal category keys to the Isotope filter class names used by the
# live europack.gr theme, so the "All Categories / Consumables / Food industry /
# Coffee production / Pharmaceutical industry" filter buttons work identically.
CATEGORY_ISOTOPE = {
    "consumables": "analwsima",
    "food": "viomixania_trofimwn",
    "coffee": "paragwgi_kafe",
    "pharma": "farmakoviomixania",
    "quality": "poiotikos_elegxos",
    "manufacturing": "paragogi-kai-syskeuasia",
    "supply": "efodiastiki_alysida",
}

for _b in BRANDS:
    _b["iso"] = " ".join(CATEGORY_ISOTOPE[c] for c in _b["categories"] if c in CATEGORY_ISOTOPE)


# Real product-photo thumbnails used on the live "Αντιπροσωπείες" archive pages
# (europack.gr agency category listings). These differ from the local brand
# LOGOS in static/images/brands/ — the archive grid shows equipment photos.
# Hotlinked to the client's own WordPress media library so they display exactly
# like the live site without any local download.
_ARCHIVE_THUMB_BASE = "https://europack.gr/wp-content/uploads/"
ARCHIVE_THUMBS = {
    "all-fill": "2025/06/thumbnail_all_fill-1.webp",
    "alu-sense": "2025/07/banner-5.png",
    "ceia": "2025/06/thumbnail_ceia.webp",
    "ceia-2": "2025/08/bk011-6.jpg",
    "claranor": "2025/07/claranor-cup-sterilization-unit-300-dpi1-1200x675-1-e1753960926204.png",
    "colombini": "2025/07/MAC3_degassing_2024_02-scaled.jpg",
    "detectamet": "2025/07/metal-detectable-stationery-e1753960854827.png",
    "econocorp": "2025/07/Econocorp.png",
    "endoline": "2025/07/Endoline.png",
    "fette-compacting": "2025/07/Fette-Compacting.png",
    "geyssel": "2025/07/applikator-457.jpg",
    "glatt-group": "2025/07/Granulation-line-scaled.jpg",
    "heat-and-control": "2025/07/conveying_index.jpg",
    "ima-ilapak": "2025/06/FVFSK25_0001_VEGATRONIC-6000-DZ_Generale-_I23.jpg",
    "ishida": "2025/06/thumbnail_ishida.webp",
    "mpac": "2025/06/Cartoning-Maestro-c-hero.jpg",
    "oli": "2025/07/kartonverpackung_-1-e1753880388360.jpg",
    "packline": "2025/07/hummus_pxm.jpg",
    "pharma-technology": "2025/07/Pharma-Technolgy.png",
    "probat": "2025/07/Probat.png",
    "sig-group": "2025/06/thumbnail_sig_group.webp",
    "sollas": "2025/07/Sollas.png",
    "supura": "2025/07/Supura.png",
    "swiss-can-machinery": "2025/07/lead.jpg",
    "tecma-aries": "2025/06/thumbnail_tecma_aries.webp",
    "volpak": "2025/07/2522-2522.jpg",
    "stommpy": "2025/06/thumbnail_stommpy.webp",
}

for _b in BRANDS:
    _thumb = ARCHIVE_THUMBS.get(_b["slug"])
    _b["archive_img"] = (_ARCHIVE_THUMB_BASE + _thumb) if _thumb else _b["img"]


def brands_by_category(category):
    """Return brand dicts tagged with the given category."""
    return [b for b in BRANDS if category in b["categories"]]


_BRANDS_BY_SLUG = {b["slug"]: b for b in BRANDS}

# Exact card order used by the live homepage "Αντιπροσωπείες / Reliable
# quality!" agencies section (europack.gr/en/), which shows product photos
# (not logos) with an arrow, the agency category label, and the brand name.
BRAND_STRIP_ORDER = [
    "ceia-2", "supura", "geyssel", "detectamet", "pharma-technology",
    "glatt-group", "fette-compacting", "alu-sense", "colombini", "probat",
    "endoline", "sollas", "volpak", "oli", "packline", "heat-and-control",
    "econocorp", "claranor", "swiss-can-machinery", "stommpy", "ishida",
    "all-fill", "ceia", "tecma-aries", "mpac", "ima-ilapak", "sig-group",
]

# On the homepage cards the label is the AGENCY category (not the industry
# sub-category), matching the live site: "Product Manufacturing and Packaging",
# "Quality control", or "Supply Chain".
AGENCY_CAT_LABELS = {
    "manufacturing": "Product Manufacturing and Packaging",
    "quality": "Quality control",
    "supply": "Supply Chain",
}


def brand_logo_strip():
    """Build the ordered homepage agencies cards, same as the live site.

    Each entry carries the real product-photo thumbnail (archive_img), the
    agency category label(s), and the brand name, in the live card order.
    """
    strip = []
    for slug in BRAND_STRIP_ORDER:
        brand = _BRANDS_BY_SLUG.get(slug)
        if not brand:
            continue
        agency = [AGENCY_CAT_LABELS[c] for c in brand["categories"] if c in AGENCY_CAT_LABELS]
        label = "  ".join(agency) if agency else "Agencies"
        strip.append({
            "name": brand["name"],
            "slug": brand["slug"],
            "img": brand.get("archive_img") or brand["img"],
            "link": brand["link"],
            "category_label": label,
        })
    return strip


TEAM = [
    {"name": "Alexandros Paraskevaidis", "role": "Company CEO", "email": "a.paraskevaidis@europack.gr"},
    {"name": "Giannis Christopoulos", "role": "Sales Engineer", "email": "i.christopoulos@europack.gr"},
    {"name": "Giorgos Flessas", "role": "Sales Engineer", "email": "g.flessas@europack.gr"},
    {"name": "Antonis Diamantopoulos", "role": "Customer Service Specialist, SIG", "email": "a.diamantopoulos@europack.gr"},
    {"name": "Vasilis Petrongonas", "role": "Technical Support Manager", "email": "v.petrongonas@europack.gr"},
    {"name": "Markos Tzivaridis", "role": "New Project Engineer", "email": "m.tzivaridis@europack.gr"},
    {"name": "Nikos Potiris", "role": "Sales Engineer", "email": "n.potiris@europack.gr"},
    {"name": "Konstantina Marinaki", "role": "Sales & Project Administration"},
    {"name": "Smaragda Getsopoulou", "role": "Sales & Project Administration"},
    {"name": "Chrysa Baka", "role": "Sales & Project Administration"},
    {"name": "Vasiliki Michopoulou", "role": "Sales & Project Administration"},
    {"name": "Eleni Golfi", "role": "Sales & Project Administration"},
    {"name": "Vangelis Kiros", "role": "Field Technician"},
    {"name": "Apostolos Dimitropoulos", "role": "Field Technician"},
    {"name": "Dimitris Argiropoulos", "role": "Field Technician"},
    {"name": "Sotiris Siakaras", "role": "Field Technician"},
    {"name": "Panagiotis Tasiopoulos", "role": "Field Technician"},
    {"name": "Thomas Fakas", "role": "Field Technician"},
    {"name": "Akis Masouros", "role": "Stommpy Sales", "email": "t.masouros@europack.gr"},
]

CONTACT_DIRECTORY = [
    {"department": "Management", "name": "Alexandros Paraskevaidis", "email": "a.paraskevaidis@europack.gr"},
    {"department": "Sales", "name": "Giannis Christopoulos", "email": "i.christopoulos@europack.gr"},
    {"department": "Sales", "name": "Giorgos Flessas", "email": "g.flessas@europack.gr"},
    {"department": "Sales", "name": "Nikos Potiris", "email": "n.potiris@europack.gr"},
    {"department": "Sales (Stommpy)", "name": "Akis Masouros", "email": "t.masouros@europack.gr"},
    {"department": "SIG Europack Service", "name": "Antonis Diamantopoulos", "email": "a.diamantopoulos@europack.gr"},
    {"department": "Technical Coordination", "name": "Vasilis Petrongonas", "email": "v.petrongonas@europack.gr"},
    {"department": "New Projects", "name": "Markos Tzivaridis", "email": "m.tzivaridis@europack.gr"},
]

NEWS = [
    {
        "title": "Interpack 2026",
        "excerpt": "Europack will be present at Interpack 2026, the world's leading trade fair for packaging and process technology.",
        "img": "https://europack.gr/wp-content/uploads/2026/03/%CE%95%CE%B9%CE%BA%CF%8C%CE%BD%CE%B11-e1774528786660.jpg",
        "link": "https://europack.gr/en/interpack-2026/",
    },
    {
        "title": "Growth Over 10% Again This Year, Driven by Yogurt, Coffee and Pharmaceutical Sector",
        "excerpt": "Europack continues its strong growth trajectory, driven by increased demand across the yogurt, coffee production, and pharmaceutical sectors.",
        "img": "https://europack.gr/wp-content/uploads/2025/12/DSC_0324-scaled.jpg",
        "link": "https://europack.gr/en/%ce%b1%ce%bd%ce%b1%cf%80%cf%84%cf%85%ce%be%ce%b7-%ce%b1%ce%bd%cf%89-%cf%84%ce%bf%cf%85-10-%ce%ba%ce%b1%ce%b9-%cf%86%ce%b5%cf%84%ce%bf%cf%83-%ce%bc%ce%b5-%cf%89%ce%b8%ce%b7%cf%83%ce%b7-%ce%b1%cf%80/",
    },
    {
        "title": "Damavand Strengthens Production Capabilities With New Aseptic Carton Filling Machine From SIG",
        "excerpt": "Iranian food producer Damavand expands its production capabilities with a new aseptic carton filling machine supplied by SIG, in partnership with Europack.",
        "img": "https://europack.gr/wp-content/uploads/2025/12/0126_2025_Damavand_TomatoProducts_PR_00_RGB_final.png",
        "link": "https://europack.gr/en/%ce%b7-damavand-%cf%85%cf%80%ce%b5%cf%81%ce%b4%ce%b9%cf%80%ce%bb%ce%b1%cf%83%ce%b9%ce%ac%ce%b6%ce%b5%ce%b9-%cf%84%ce%b7%ce%bd-%cf%80%ce%b1%cf%81%ce%b1%ce%b3%cf%89%ce%b3%ce%b9%ce%ba%ce%ae-%cf%84%ce%b7/",
    },
    {
        "title": "SIG Presents the SIG Terra Packaging Portfolio",
        "excerpt": "SIG introduces the SIG Terra alu-free, full-barrier, multi-serve carton packaging portfolio for sustainable food and beverage packaging.",
        "img": "https://europack.gr/wp-content/uploads/2025/08/sig-terra-alu-free-full-barrier-multi-serve-rgb.jpg",
        "link": "https://europack.gr/en/%ce%b7-sig-%cf%80%ce%b1%cf%81%ce%bf%cf%85%cf%83%ce%b9%ce%ac%ce%b6%ce%b5%ce%b9-%cf%84%ce%b9%cf%82-%cf%83%cf%85%cf%83%ce%ba%ce%b5%cf%85%ce%b1%cf%83%ce%af%ce%b5%cf%82-sig-terra-alu-free/",
    },
    {
        "title": "The Industry at a Crossroads",
        "excerpt": "A look at how the packaging and food processing industry is navigating sustainability, automation and shifting consumer demand.",
        "img": "https://europack.gr/wp-content/uploads/2025/08/Screenshot-2025-08-19-161546_1-e1755610859630.png",
        "link": "https://europack.gr/en/%ce%b7-%ce%b2%ce%b9%ce%bf%ce%bc%ce%b7%cf%87%ce%b1%ce%bd%ce%af%ce%b1-%cf%83%ce%b5-%ce%ba%cf%81%ce%af%cf%83%ce%b9%ce%bc%ce%bf-%cf%83%cf%84%ce%b1%cf%85%cf%81%ce%bf%ce%b4%cf%81%cf%8c%ce%bc%ce%b9/",
    },
    {
        "title": "MEVGAL",
        "excerpt": "Europack partners with MEVGAL, one of the leading dairy producers in Greece, on production and packaging equipment.",
        "img": "https://europack.gr/wp-content/uploads/2025/07/Picture1.png",
        "link": "https://europack.gr/en/mevgal/",
    },
]
