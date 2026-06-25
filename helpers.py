import requests

from flask import redirect, render_template, session
from functools import wraps
from datetime import date
import calendar

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

def problem(message, code=400):
    """Render message as an apology to user."""

    return render_template("problem.html", message=message, code=code)


def get_days():
    today = date.today()

    return calendar.monthrange(today.year, today.month)[1]


def get_month():
    today = date.today()

    return calendar.month_name[today.month]
