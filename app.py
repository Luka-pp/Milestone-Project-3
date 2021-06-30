import os
import math
from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route("/bikes")
def bike():
    bikes = mongo.db.bikes.find()
    return render_template("index.html", bikes=bikes)


@app.route('/members')
def members():
    per_page = 4
    page = int(request.args.get("page", 1))
    total = mongo.db.bikes.count_documents({})
    all_bikes = mongo.db.bikes.find().skip((page - 1)*per_page).limit(per_page)
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    return render_template("members.html", bikes=all_bikes, pages=pages, page=page, total=total)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.user.find_one({"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.user.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.user.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_bike", methods=["GET", "POST"])
def add_bike():
    if request.method == "POST":
        bike = {
            "img_url": request.form.get("img_url"),
            "nickname": request.form.get("nickname"),
            "make": request.form.get("make"),
            "model": request.form.get("model"),
            "helmet": request.form.get("helmet"),
            "jacket": request.form.get("jacket"),
            "trousers": request.form.get("trousers"),
            "boots": request.form.get("boots"),
            "gloves": request.form.get("gloves"),
            "routestart": request.form.get("routestart"),
            "routevia": request.form.get("routevia"),
            "routeend": request.form.get("routeend"),
            "owner": session["user"]
        }
        mongo.db.bikes.insert_one(bike)
        flash("Bike successfully created!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("add_bike.html")


@app.route("/edit_bike/<bike_id>", methods=["GET", "POST"])
def edit_bike(bike_id):
    bike = mongo.db.find_one({"_id": ObjectId(bike_id)})
    return render_template("edit_bike.html", bike=bike)


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
