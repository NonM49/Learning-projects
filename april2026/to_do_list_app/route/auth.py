from flask import (Blueprint, render_template, request,
                    flash, redirect, session, url_for)
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        c_password = request.form["c_password"]

        if len(password) < 6:
            flash("Password must be at least 6 characters.", "danger")
            return render_template("register.html", username=username)
        
        if password != c_password:
            flash("password not match", "danger")
            return render_template(
                "register.html",
                username=username
            )
        
        hashed_password = generate_password_hash(password)
        
        conn = sqlite3.connect("database.db", check_same_thread=False)
        cur = conn.cursor()

        # check if user exists
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cur.fetchone()

        if user:
            flash("Username already exists", "danger")
            return render_template("register.html", username=username)
        
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()
        conn.close()
        flash("User registered!", "success")

        return redirect("/login")
    
    # if GET request render template
    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cur.fetchone()
        print(user)

        conn.close()

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]
            username = session.get("username")

            flash(f"login successful, {username}.", "success")
            return redirect(url_for("home.dash"))
        else:
            flash("Invalid username or password", "danger")
            return render_template("login.html")
        
    return render_template("login.html")

@auth.route("/logout")
def logout():
    username = session.get("username")
    session.pop("username", None) #None is the defalt value if the key doesn't exists
    session.pop("user_id", None)

    flash(f"Logged out successful!, {username} ", "success")
    return redirect(url_for("home.dash"))

