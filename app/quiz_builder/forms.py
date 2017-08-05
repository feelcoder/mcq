# Import Form and RecaptchaField (optional)
from flask_wtf import Form  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, IntegerField, SelectField, DateTimeField, HiddenField # BooleanField

# Import Form validators
from wtforms.validators import Required, Length


# Define the login form (WTForms)

class QuizAddForm(Form):
    title = TextField('Title', [
                Required('Title cannot be left blank'), Length(4, 200, "Title should be a minimum of 4 letters")])
    instruction = TextField('Instruction', [])
    time = IntegerField('Time (mins)', [
                Required('Title cannot be left blank')])
    visibility = SelectField(
        'Visibility', [('pv', 'Private'), ('pu', 'Public')])
    start = DateTimeField('Start time', Required('Time quiz starts must be specifeid')])
    uid= HiddenField()
