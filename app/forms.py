from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email,EqualTo

class SignupForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  email = StringField("email", validators=[DataRequired(),Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])

class SigninForm(FlaskForm):
  email = StringField("email", validators=[DataRequired(),Email()])
  password = PasswordField("Password", validators=[DataRequired()])