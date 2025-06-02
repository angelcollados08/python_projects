from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
# from forms import *
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
#from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import os
import random
from datetime import date



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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///check.db'
app.config['SECRET_KEY'] = "gergrgrtgrtg"
db = SQLAlchemy(model_class=Base)
ckeditor = CKEditor(app)
Bootstrap5(app)

today = date.today()

db.init_app(app)


# Cafe TABLE Configuration
class Check(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    due_date: Mapped[str] = mapped_column(Boolean, nullable=False)
    has_start: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_color: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_done: Mapped[bool] = mapped_column(Boolean, nullable=False)

    
#     def to_dict(self):
#             #Method 1. 
#             # Loop through each column in the data recor
            
#             #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
#         return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Check))
    all_check = result.scalars().all()
    return render_template("index.html",date = today.strftime("%d/%m/%Y"), all_check = all_check)


@app.post("/new_task")
def new_task():
    # result = db.session.execute(db.select(Cafe))
    # all_cafes = result.scalars().all()
    data = request.form
    new_check = Check(
            name=data["input_task"],
            due_date=False,
            has_start=False,
            has_color=False,
            is_done=False,
        )
    db.session.add(new_check)
    db.session.commit()
    return redirect(url_for("home"))   

@app.route("/mark_check/<int:check_id>")
def mark_check(check_id):
    print('here')
    check = db.get_or_404(Check, check_id)
    # all_cafes = result.scalars().all()
    check.is_done = True
    db.session.commit()
    return redirect(url_for("home"))   





if __name__ == '__main__':
    app.run(debug=True)
