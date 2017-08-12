# Import Form and RecaptchaField (optional)
from flask_wtf import Form # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField, StringField, TextAreaField  # BooleanField

# Import Form validators

from wtforms.validators import Required, Email, EqualTo, Length, DataRequired


# Define the login form (WTForms)

class LoginForm(Form):
    email    = TextField('Email Address', [Email(),
                Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
                Required(message='Must provide a password. ;-)')])


# Register Form Class
class RegisterForm(Form):
    first_name = TextField('First Name')
    last_name = TextField('Last Name')
    #name = StringField('Name', [validators.Length(min=1, max=50)])
    username = TextField('Username' )
    email = TextField('Email')
    password = PasswordField('Password')
    confirm = PasswordField('Confirm Password')