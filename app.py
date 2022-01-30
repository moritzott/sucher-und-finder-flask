from flask import Flask, render_template
from admin.admin_pages import admin_pages
from errors.error_pages import error_pages
from settings.contact_config import contact_data


app = Flask(__name__)


# Blueprints mit Routen werden registriert:
app.register_blueprint(admin_pages, url_prefix="/admin")
app.register_blueprint(error_pages, url_prefix="/error")

# Index-Page_
@app.route("/home", methods=["GET"])
@app.route("/", methods=["GET"])
def index():
    return render_template("home.html")

# Login or register:
@app.route("/login-or-register", methods=["GET"])
def log_or_reg():
    return render_template("login-or-register.html")

# Login Page:
@app.route("/login", methods=["GET"])
def login():
    # noch abfangen: wenn der Nutzer schon angemeldet ist, dann direkt zur welcome
    # page umleiten! ansonsten return render_template!
    return render_template("login.html")

# Hilfe-Seite:
@app.route("/help", methods=["GET"])
def help():
    contact_info = contact_data
    return render_template("help.html", contact = contact_info)

# Captcha-Abfrage beim Registrieren
@app.route("/captcha/check", methods=["GET"])
def captcha_check():
    return render_template("/captcha/check.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)