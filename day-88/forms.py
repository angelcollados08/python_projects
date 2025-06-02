from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    map_url = StringField("Cafe Map URL", validators=[DataRequired(), URL()])
    location = StringField("Cafe Location", validators=[DataRequired()])
    has_sockets = StringField("Has sockets? (Y/N)", validators=[DataRequired()])
    has_toilet = StringField("Has toilets? (Y/N)", validators=[DataRequired()])
    has_wifi = StringField("Has wifi? (Y/N)", validators=[DataRequired()])
    can_take_calls = StringField("Can take calls? (Y/N)", validators=[DataRequired()])
    seats = StringField("Seats", validators=[DataRequired()])
    coffee_price = StringField("Coffe price", validators=[DataRequired()])
    submit = SubmitField("Submit Post")



# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
