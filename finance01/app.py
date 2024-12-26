import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import pandas as pd

from helpers import apology, login_required, lookup, usd

#NOTES - implement sell function (specifically receiving money function), implement delete function for to delete used values
#, implement history function with CSS table

# Configure application
app = Flask(__name__)
app.secret_key = "Hello_world"

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.errorhandler(400)
def handle_bad_request(error):
    return render_template('login.html', error='400 Bad Request'), 400

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def getsharecount(shares):
    entry = {}

    for share in shares:
        x = share['share']
        entry[x] = 0

    for share in shares:
        y = share['share']
        x = share['amount']
        entry[y] += x

    filtered_data = {key: value for key, value in entry.items() if value != 0}

    print(filtered_data)

    return filtered_data

def updatesharecount(entry):

    db.execute("DELETE FROM sharecount WHERE id=?", session["user_id"])

    for shares in entry:
        share = shares
        count = entry[shares]
        db.execute("INSERT INTO sharecount (share, count,id) VALUES (?,?,?)", share, count, session["user_id"])

    return

@app.route("/")
@login_required
def index():

    list_of_shares = []
    entry = {}
    entry2 = {}

    shares = db.execute("SELECT share, amount FROM shares WHERE id = ?", session["user_id"])

    #Two for loops to find out the count of sharrs

    entry = getsharecount(shares)

    updatesharecount(entry)

    for entries in entry:
        share = entries
        amount = entry[entries]
        price = lookup(entries)
        price = price['price']
        total = price * amount

        entry2['share'] = share
        entry2['amount'] = amount
        entry2['price'] = price
        entry2['total'] = round(total,2)
        list_of_shares.append(entry2)
        entry2 = {}

    final = {}

    balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    final['balance'] = round(balance[0]['cash'], 2)
    final['total'] = 0

    for total in list_of_shares:
        final['total'] += total['total']

    final['total'] += final['balance']
    final['total'] = round(final['total'], 2)

    """Show portfolio of stocks"""
    return render_template("main.html", list_of_shares=list_of_shares, final=final)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "POST":

        shares = request.form.get("shares");
        symbol = request.form.get("symbol");

        if not shares.isdigit():
            return "can't purchase partial sales", 400

        if(int(shares) < 0 or shares.isnumeric() == False):
            return "INCORRECT SHARE data", 400

        response = lookup(symbol)

        if(response == None):
            return apology("Incorrect symbol bro")

        price = response['price']

        cost = price * int(shares)

        #GET amount of money from the database

        money = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        money = money[0]['cash']

        newcash = money - cost
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if(money>cost):
            db.execute("UPDATE users SET cash=? WHERE id=?", newcash, session["user_id"])
            db.execute("INSERT INTO shares (id, share, amount, time_bought) VALUES (?,?,?,?)", session["user_id"], symbol, shares, current_datetime)
            db.execute("INSERT INTO sharecount (id) VALUES (?)", session["user_id"])
            flash("Purchase successful")
            return redirect("/")
        else:
            return apology("You're broke. Not enough cash")

        #IF money is more than the cost, then execute the db

        #db which is first minus the money from the bank account
        #second add the shares to the database, based on session id
        #third is to add the time to the databse

        return render_template("main.html")

    else:
        return render_template("buy.html")


    """Buy shares of stock"""

@app.route("/history")
@login_required
def history():

    history = db.execute("SELECT share, amount, time_bought FROM shares WHERE id = ?", session["user_id"])

    print(history)

    """Show history of transactions"""
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Login successful")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        message = request.args.get('message')

        if(message):
            flash(message)

        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form

    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol");
        response = lookup(symbol)

        if(response == None):
            return apology("Incorrect symbol bro")

        price = response['price']

        return render_template("quoted.html",name=response['name'], price=response['price'],symbol=response['symbol'])

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username");
        password = request.form.get("password");
        password2 = request.form.get("confirmation");

        checkuser = db.execute("SELECT username FROM users")

        for x in checkuser:
            if(x['username'] == username):
                flash("Username already exists")
                return abort(400)

        if(username.strip() == "" or password.strip() == "" or password2.strip() == ""):
            flash("Empty fields")
            return abort(400)

        if(password != password2):
            flash("Password do not match")
            return abort(400)

        else:
            new_password = generate_password_hash(password)
            print(new_password)
            db.execute("INSERT INTO users (username,hash) VALUES(?,?)", username,new_password)
            flash("User registration successful")
            return render_template("login.html")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    shares = db.execute("SELECT share, amount FROM shares WHERE id = ?", session["user_id"])
    entry = getsharecount(shares)

    if request.method == "POST":

        count = request.form.get("shares")
        count = int(count)
        symbol = request.form.get("symbol")

        cost = lookup(symbol)
        cost = cost['price']
        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        current_cash = current_cash[0]['cash']

        total_cost = cost * count

        if(entry[symbol] >=count):
            count = -count
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db.execute("INSERT INTO shares (id, share, amount, time_bought) VALUES (?,?,?,?)", session["user_id"], symbol, count, current_datetime)
            new_cash = current_cash + total_cost
            db.execute("UPDATE users SET cash=? WHERE id=?", new_cash, session["user_id"])
            flash("Successfully sold!")
            return redirect('/')

        else:
            return apology("You don't have enough shares to sell")

    else:

        return render_template("sell.html", entry=entry)

@app.route("/buymain", methods=["POST"])
@login_required
def buymain():

    form_id = request.form.get('form_id')

    buysell_string = "buysell" + form_id
    buysell = request.form.get(buysell_string)

    amount_string = "amount" + form_id
    amount = request.form.get(amount_string)
    amount = int(amount)

    x = db.execute("SELECT share, count FROM sharecount WHERE id = ?", session["user_id"])
    index = int(form_id) - 1
    symbol = x[index]['share']

    current_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    current_cash = current_cash[0]['cash']

    price_per_symbol = lookup(symbol)
    price_per_symbol = price_per_symbol['price']
    cost = price_per_symbol * amount

    stockcount = x[index]['count']

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if(buysell == "buy"):
        if(current_cash >= cost):
            new_cash = current_cash - cost
            db.execute("UPDATE users SET cash=? WHERE id=?", new_cash, session["user_id"])
            db.execute("INSERT INTO shares (id, share, amount, time_bought) VALUES (?,?,?,?)", session["user_id"], symbol, amount, current_datetime)
            flash("Purchase successful")
            return redirect("/")

        else:
            return apology("Not enough cash")

    if(buysell=="sell"):
        if(stockcount >= amount):
            new_cash = current_cash + cost
            amount = -amount
            db.execute("UPDATE users SET cash=? WHERE id=?", new_cash, session["user_id"])
            db.execute("INSERT INTO shares (id, share, amount, time_bought) VALUES (?,?,?,?)", session["user_id"], symbol, amount, current_datetime)
            flash("Shares sold")
            return redirect("/")
        else:
            return apology("Selling too many stocks you don't own")

    return apology("Just testing out bro")