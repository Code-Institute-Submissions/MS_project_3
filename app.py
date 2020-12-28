import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


#home page
@app.route("/")
@app.route("/index")
def index():
    endangered_birds = list(mongo.db.endangered_birds.find())
    return render_template("index.html",
        endangered_birds=endangered_birds)


@app.route("/view_bird/<bird_id>")
def view_bird(bird_id):
    endangered_bird = mongo.db.endangered_birds.find_one(
        {"_id": ObjectId(bird_id)})

    return render_template("endangered_bird.html",
        endangered_bird=endangered_bird)


#register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

#register the new user
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for('add_sightings', username=session["user"]))
    return render_template("register.html")


#login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for('add_sightings',
                        username=session["user"]))
            else:
                #invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


#log out page
@app.route("/logout")
def logout():
    # remove user's cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/my_sightings")
def my_sightings():
    user_sightings = list(mongo.db.sightings.find())
    return render_template("my_sightings.html", sightings=user_sightings)


@app.route("/add_sightings", methods=["GET", "POST"])
def add_sightings():
    if request.method == "POST":
        sightings = {
            "name": request.form.get("name"),
            "location": request.form.get("location"),
            "date": request.form.get("date"),
            "comment": request.form.get("comment"),
            "created_by": session["user"]
        }
        mongo.db.sightings.insert_one(sightings)
        flash("Sighting is Successfully Added")

    bird_name = mongo.db.endangered_birds.find()
    city = mongo.db.locations.find()
    return render_template("add_sightings.html",
        endangered_birds=bird_name, locations=city)


@app.route("/edit_sighting/<sighting_id>", methods=["GET", "POST"])
def edit_sighting(sighting_id):
    if request.method == "POST":
        update = {
            "name": request.form.get("name"),
            "location": request.form.get("location"),
            "date": request.form.get("date"),
            "comment": request.form.get("comment"),
            "created_by": session["user"]
        }
        mongo.db.sightings.update({"_id": ObjectId(sighting_id)}, update)
        flash("Sighting is Successfully Updated")

    sighting = mongo.db.sightings.find_one({"_id": ObjectId(sighting_id)})
    bird_name = mongo.db.endangered_birds.find()
    city = mongo.db.locations.find()
    return render_template("edit_sightings.html",
        sighting=sighting, endangered_birds=bird_name, locations=city)


@app.route("/delete_sighting/<sighting_id>")
def delete_sighting(sighting_id):
    mongo.db.sightings.remove({"_id": ObjectId(sighting_id)})
    flash("Sighting is Successfully Deleted")
    return redirect(url_for("my_sightings"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)