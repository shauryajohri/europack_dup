"""Real content sourced from the live europack.gr site: represented brands,
team members, news articles, and contact directory. Images are hotlinked to
the client's own WordPress media library (europack.gr/wp-content/uploads/...).
"""

BRANDS = [
    {"name": "All-Fill", "slug": "all-fill", "img": "https://europack.gr/wp-content/uploads/2025/06/thumbnail_all_fill-1.webp", "link": "https://europack.gr/en/antiprosopeia/all-fill/", "categories": ["food", "manufacturing"]},
    {"name": "AluSense", "slug": "alu-sense", "img": "https://europack.gr/wp-content/uploads/2025/07/banner-5.png", "link": "https://europack.gr/en/antiprosopeia/alu-sense/", "categories": ["manufacturing", "coffee"]},
    {"name": "CEIA", "slug": "ceia", "img": "/static/images/site/metal-detector-line.jpg", "link": "https://europack.gr/en/antiprosopeia/ceia/", "categories": ["food", "manufacturing", "quality"]},
    {"name": "CEIA", "slug": "ceia-2", "img": "/static/images/site/portable-metal-detector.jpg", "link": "https://europack.gr/en/antiprosopeia/ceia-2/", "categories": ["manufacturing", "pharma"]},
    {"name": "Claranor", "slug": "claranor", "img": "https://europack.gr/wp-content/uploads/2025/07/claranor-cup-sterilization-unit-300-dpi1-1200x675-1-e1753960926204.png", "link": "https://europack.gr/en/antiprosopeia/claranor/", "categories": ["food", "manufacturing", "pharma"]},
    {"name": "Colombini", "slug": "colombini", "img": "https://europack.gr/wp-content/uploads/2025/07/MAC3_degassing_2024_02-scaled.jpg", "link": "https://europack.gr/en/antiprosopeia/colombini/", "categories": ["manufacturing", "coffee"]},
    {"name": "Detectamet", "slug": "detectamet", "img": "/static/images/site/detectamet-product.jpg", "link": "https://europack.gr/en/antiprosopeia/detectamet/", "categories": ["consumables", "manufacturing"]},
    {"name": "Econocorp", "slug": "econocorp", "img": "https://europack.gr/wp-content/uploads/2025/07/Econocorp.png", "link": "https://europack.gr/en/antiprosopeia/econocorp/", "categories": ["food", "manufacturing"]},
    {"name": "Endoline", "slug": "endoline", "img": "/static/images/site/endoline-logo.png", "link": "https://europack.gr/en/antiprosopeia/endoline/", "categories": ["food", "manufacturing"]},
    {"name": "Fette Compacting", "slug": "fette-compacting", "img": "https://europack.gr/wp-content/uploads/2025/07/Fette-Compacting.png", "link": "https://europack.gr/en/antiprosopeia/fette-compacting/", "categories": ["manufacturing", "pharma"]},
    {"name": "GEYSSEL", "slug": "geyssel", "img": "https://europack.gr/wp-content/uploads/2025/07/applikator-457.jpg", "link": "https://europack.gr/en/antiprosopeia/geyssel/", "categories": ["food", "manufacturing"]},
    {"name": "Glatt Group", "slug": "glatt-group", "img": "https://europack.gr/wp-content/uploads/2025/07/Granulation-line-scaled.jpg", "link": "https://europack.gr/en/antiprosopeia/glatt-group/", "categories": ["manufacturing", "pharma"]},
    {"name": "Heat and Control", "slug": "heat-and-control", "img": "https://europack.gr/wp-content/uploads/2025/07/conveying_index.jpg", "link": "https://europack.gr/en/antiprosopeia/heat-and-control/", "categories": ["food", "manufacturing"]},
    {"name": "IMA Ilapak", "slug": "ima-ilapak", "img": "https://europack.gr/wp-content/uploads/2025/06/FVFSK25_0001_VEGATRONIC-6000-DZ_Generale-_I23.jpg", "link": "https://europack.gr/en/antiprosopeia/ima-ilapak/", "categories": ["food", "manufacturing"]},
    {"name": "Ishida", "slug": "ishida", "img": "/static/images/site/xray-inspection.png", "link": "https://europack.gr/en/antiprosopeia/ishida/", "categories": ["food", "manufacturing", "quality", "pharma"]},
    {"name": "Mpac", "slug": "mpac", "img": "https://europack.gr/wp-content/uploads/2025/06/Cartoning-Maestro-c-hero.jpg", "link": "https://europack.gr/en/antiprosopeia/mpac/", "categories": ["food", "manufacturing"]},
    {"name": "Oli", "slug": "oli", "img": "https://europack.gr/wp-content/uploads/2025/07/kartonverpackung_-1-e1753880388360.jpg", "link": "https://europack.gr/en/antiprosopeia/oli/", "categories": ["food", "manufacturing"]},
    {"name": "Packline", "slug": "packline", "img": "https://europack.gr/wp-content/uploads/2025/07/hummus_pxm.jpg", "link": "https://europack.gr/en/antiprosopeia/packline/", "categories": ["food", "manufacturing"]},
    {"name": "Pharma Technology", "slug": "pharma-technology", "img": "https://europack.gr/wp-content/uploads/2025/07/Pharma-Technolgy.png", "link": "https://europack.gr/en/antiprosopeia/pharma-technology/", "categories": ["manufacturing", "pharma"]},
    {"name": "Probat", "slug": "probat", "img": "/static/images/site/probat-roasters.png", "link": "https://europack.gr/en/antiprosopeia/probat/", "categories": ["manufacturing", "coffee"]},
    {"name": "SIG Group", "slug": "sig-group", "img": "/static/images/site/sig-facility.png", "link": "https://europack.gr/en/antiprosopeia/sig-group/", "categories": ["food", "manufacturing"]},
    {"name": "Sollas", "slug": "sollas", "img": "https://europack.gr/wp-content/uploads/2025/07/Sollas.png", "link": "https://europack.gr/en/antiprosopeia/sollas/", "categories": ["food", "manufacturing"]},
    {"name": "Supura", "slug": "supura", "img": "https://europack.gr/wp-content/uploads/2025/07/Supura.png", "link": "https://europack.gr/en/antiprosopeia/supura/", "categories": ["food", "manufacturing"]},
    {"name": "Swiss Can Machinery", "slug": "swiss-can-machinery", "img": "https://europack.gr/wp-content/uploads/2025/07/lead.jpg", "link": "https://europack.gr/en/antiprosopeia/swiss-can-machinery/", "categories": ["food", "manufacturing"]},
    {"name": "Tecma Aries", "slug": "tecma-aries", "img": "https://europack.gr/wp-content/uploads/2025/06/thumbnail_tecma_aries.webp", "link": "https://europack.gr/en/antiprosopeia/tecma-aries/", "categories": ["food", "manufacturing"]},
    {"name": "Volpak", "slug": "volpak", "img": "https://europack.gr/wp-content/uploads/2025/07/2522-2522.jpg", "link": "https://europack.gr/en/antiprosopeia/volpak/", "categories": ["food", "manufacturing"]},
    {"name": "Stommpy", "slug": "stommpy", "img": "/static/images/site/warehouse-barriers.png", "link": "https://europack.gr/en/antiprosopeia/stommpy/", "categories": ["supply"]},
]

CATEGORY_LABELS = {
    "manufacturing": "Product Manufacturing & Packaging Lines",
    "quality": "Quality Control",
    "supply": "Supply Chain",
    "food": "Food Industry",
    "coffee": "Coffee Production",
    "pharma": "Pharmaceutical Industry",
    "consumables": "Consumables",
}


def brands_by_category(category):
    """Return brand dicts tagged with the given category."""
    return [b for b in BRANDS if category in b["categories"]]


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
