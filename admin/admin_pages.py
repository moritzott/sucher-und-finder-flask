from flask import Blueprint, render_template

# Das hier ist der Blueprint für den Admin-Bereich
# ------------------------------------------------

admin_pages = Blueprint("admin_pages", __name__, static_folder="static", template_folder="templates")

@admin_pages.route("/home", methods=["GET"])
@admin_pages.route("/", methods=["GET"])
def home():
    return render_template("/admin/home.html")