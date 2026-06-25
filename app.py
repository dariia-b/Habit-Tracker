import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date

from helpers import login_required, get_days, get_month

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///habits.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user = session.get("user_id")
    today = date.today()
    count_total = 0
    count_today = 0

    habits = db.execute("SELECT id, name, tag, user_id FROM habits WHERE user_id = ?", user)
    today_habits = db.execute("SELECT * FROM completions WHERE user_id = ? AND date = ?", user, today)
    for habit in habits:
        rows = db.execute("SELECT 1 FROM completions WHERE habit_id = ? AND date = ? AND user_id = ?",
            habit["id"], today, user)
        habit["completed"] = len(rows) > 0

    for habit in habits:
        count_total += 1

    for habit in today_habits:
        count_today += 1

    if count_total != 0:
        percentage = int(count_today / count_total * 100)
    else:
        percentage = 100

    return render_template("index.html", habits = habits, count_total=count_total, count_today=count_today, percentage=percentage);


@app.route("/dashboard")
@login_required
def dashboard():
    if request.method == "GET":
        user = session.get("user_id")

        days = get_days()
        month_name = get_month()
        today = date.today()
        start = date(today.year, today.month, 1)
        end = date(today.year, today.month, days)

        habits = db.execute("SELECT habit_id, name, date FROM habits JOIN completions ON habits.id = completions.habit_id AND habits.user_id = completions.user_id WHERE date >= ? AND date <= ? AND habits.user_id = ?", start, end, user)

        habit_dashboard = []
        for habit in habits:
            found = False
            name = habit["name"]
            dates = habit["date"]
            count = 0

            for h in habit_dashboard:
                if h["name"] == name:
                    habit_dashboard[count]["date"].append(dates)
                    print(h)
                    found = True
                    print("1")
                count += 1

            if not found:
                habit_dashboard.append({"name": name, "date": []})
                last_index = len(habit_dashboard) - 1
                habit_dashboard[last_index]["date"].append(dates)

        return render_template("dashboard.html", year=today.year, month=today.month, month_name=month_name, days=days, habits=habits, dashboard = habit_dashboard, size=len(habit_dashboard)+1)

@app.route("/toggle", methods=["POST"])
@login_required
def toggle():
    id = request.form.get("habit_id")
    if not id:
        flash("Couldn't find the habit")
        return redirect("/")

    habit_id = int(id)
    today = date.today().isoformat()
    user = session.get("user_id")

    rows = db.execute("SELECT * FROM completions WHERE habit_id = ? AND date = ? AND user_id = ?",
    habit_id, today, user)


    #if the habit was already completed
    if rows:
        #undo
        db.execute("DELETE FROM completions WHERE habit_id = ? AND date = ? AND user_id = ?", habit_id, today, user)

    #if the habit wasn't completed yet
    else:
        db.execute("INSERT INTO completions (habit_id, date, user_id) VALUES (?, ?, ?)", id, today, user)


    return redirect("/")


@app.route("/edit")
@login_required
def edit():
    if request.method == "GET":
        user = session.get("user_id")
        habits = db.execute("SELECT id, name, tag FROM habits WHERE user_id = ?", user)
        return render_template("edit.html", habits = habits)

@app.route("/create", methods=["POST"])
@login_required
def create():
    user = session.get("user_id")
    if request.method == "POST":
        name = request.form.get("name")
        tag = request.form.get("tag")

        if not name:
            flash("Name cannot be empty")
            return redirect("/edit")
        elif not tag:
            tag = ""

        db.execute("INSERT INTO habits (name, tag, user_id) VALUES (?, ?, ?)", name, tag, user)

        return redirect("/edit")
    else:
        return redirect("/edit")

@app.route("/rename", methods=["POST"])
@login_required
def rename():
    if request.method == "POST":
        id = int(request.form.get("habit_id"))
        new_name = request.form.get("new_name")

        if not new_name:
            flash("New name is empty.")
            return redirect("/edit")
        elif not id:
            flash("Couldn't find the habit.")
            return redirect("/edit")

        db.execute("UPDATE habits SET name = ? WHERE id = ?", new_name, id)

        return redirect("/edit")




@app.route("/delete", methods=["POST"])
@login_required
def delete():
    if request.method == "POST":
        id = request.form.get("habit_id")
        if not id:
            flash("Couldn't find the habit.")
            return redirect("/edit")

        id = int(id)

        db.execute("DELETE FROM completions WHERE habit_id = ?", id)
        db.execute("DELETE FROM habits WHERE id = ?", id)

        return redirect("/edit")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            flash("Username is empty.")
            return redirect("/login")
        elif not request.form.get("password"):
            flash("Password is empty.")
            return redirect("/login")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("Invalid username or password.")
            return redirect("/")
        
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")


@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")

        if not name:
            flash("Name cannot be empty.")
            return redirect("/register")
        elif not password:
            flash("Password cannot be empty.")
            return redirect("/register")
        elif password != request.form.get("confirmation"):
            flash("Passwords don't match.")
            return redirect("/register")

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                       name, generate_password_hash(password))
        except ValueError:
            flash("This username is already taken.")
            return redirect("/register")

        return redirect("/login")
    else:
        return render_template("register.html")
