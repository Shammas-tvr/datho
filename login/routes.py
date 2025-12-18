from flask import render_template, request, redirect, url_for, session
from . import login_bp

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect(url_for("login.dashboard"))
        else:
            error = "Invalid credentials"

    return render_template("login.html", error=error)


@login_bp.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login.login"))
    return f"Welcome {session['user']}"
