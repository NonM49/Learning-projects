from flask import (Blueprint, render_template, request,
                    flash, redirect, session, url_for)
import sqlite3

home = Blueprint("home", __name__)

@home.route("/")
def dash():
    return render_template("home.html")

@home.route("/dashboard")
def dashboard():

    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT id, description, completed FROM to_do_list WHERE user_id=?",
        (session["user_id"],)
    )
    tasks = cur.fetchall()
    return render_template("dashboard.html", tasks=tasks)

@home.route("/add", methods=["GET", "POST"])
def add_to_do_list():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))
    
    if request.method == "POST":
        desc = request.form["description"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO to_do_list (user_id, description) VALUES (?, ?)",
            (session["user_id"], desc)
        )

        conn.commit()
        conn.close()

        flash("Added!", "success")
        return redirect(url_for("home.dashboard"))
    
    return render_template("add_to_do_list.html")

@home.route("/toggle/<int:id>", methods=["POST"])
def toggle(id):

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "UPDATE to_do_list SET completed = NOT completed WHERE id=?",
        (id,)
    )
    conn.commit()
    conn.close()

    return "", 204 # mean, no content needed to return.

@home.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM to_do_list WHERE id=?",
        (id,)
    )
    conn.commit()
    conn.close()

    return redirect("/dashboard")