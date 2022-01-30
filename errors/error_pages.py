from flask import Blueprint, render_template
from settings.contact_config import contact_data

# Blueprint für die Fehlermeldungen 
# ---------------------------------

error_pages = Blueprint("error_pages", __name__, static_folder="static", template_folder="templates")

@error_pages.route("/disallowed-request", methods=["GET"])
def disallowed_request():
    contact_info = contact_data
    return render_template("/errors/disallowed-request.html", contact = contact_info)

@error_pages.route("/not-authorized", methods=["GET"])
def not_authorized():
    return render_template("/errors/not-authorized.html")

@error_pages.route("/not-logged-in", methods=["GET"])
def not_logged_in():
    return render_template("/errors/not-logged-in.html")

@error_pages.route("/wrong-captcha", methods=["GET"])
def wrong_captcha():
    return render_template("/errors/wrong-captcha.html")