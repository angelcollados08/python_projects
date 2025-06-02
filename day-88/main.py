from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
from forms import *
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import os
import random


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SECRET_KEY'] = "gergrgrtgrtg"
db = SQLAlchemy(model_class=Base)
ckeditor = CKEditor(app)
Bootstrap5(app)

db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    
    def to_dict(self):
            #Method 1. 
            # Loop through each column in the data recor
            
            #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return render_template("index.html",all_caffes=all_cafes, name = "frege")


# HTTP GET - Read Record

@app.get("/random")
def random_caffe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify( cafe = {
                    "name":random_cafe.name,
                   "map_url":random_cafe.map_url,
                   "img_url":random_cafe.img_url,
                   "location":random_cafe.location,
                   "seats":random_cafe.seats,
                   "has_toilet":random_cafe.has_toilet,
                   "has_wifi":random_cafe.has_wifi,
                   "has_sockets":random_cafe.has_sockets,
                   "can_take_calls":random_cafe.can_take_calls,
                   "coffee_price":random_cafe.coffee_price,
                }
                   )



@app.get("/all")
def all_caffe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.get("/search")
def search_cafe():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error = {
            "Not found" : "Sorry, we don't have a cafe at the location"
        })

# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets") == "Y"),
        has_toilet=bool(request.form.get("toilet")== "Y"),
        has_wifi=bool(request.form.get("wifi")== "Y"),
        can_take_calls=bool(request.form.get("calls")== "Y"),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/new-post", methods=["GET", "POST"])
def add_new_caffe():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=(form.has_sockets.data == "Y"),
            has_toilet=(form.has_toilet.data == "Y"),
            has_wifi=(form.has_wifi.data == "Y"),
            can_take_calls=(form.can_take_calls.data == "Y"),
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("make-post.html", form=form)

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
