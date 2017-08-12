# Import Form and RecaptchaField (optional)
from flask_wtf import Form  # , RecaptchaField
import datetime
# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, IntegerField, SelectField, DateTimeField, HiddenField, FloatField, SubmitField, RadioField, FieldList, FormField, BooleanField  # BooleanField

# Import Form validators
from wtforms.validators import Required, Length


# Define the login form (WTForms)

class QuizAddForm(Form):
    title = TextField('Title', [
        Required('Title cannot be left blank'), Length(4, 200, "Title should be a minimum of 4 letters")])
    instructions = TextField('Instruction', [])
    time = IntegerField('Time (mins)', [
        Required('Title cannot be left blank')])
    total_marks = FloatField("Total marks", [Required(
        "Total quiz marks must be specified")])
    closed = SelectField(
        'Visibility', choices=[('pv', 'Private'), ('pu', 'Public')])
    start_date = DateTimeField("Start time", [Required(
        message='Time quiz starts must be specifeid')], default=datetime.datetime.now())
    submit = SubmitField("create")
    uid = HiddenField(default=1234)


class QuestionOptionForm(Form):
    answer = BooleanField(default=False)

    text = TextField()


class QuestionForm(Form):
    text = TextField('Question', [Required('Title cannot be left blank')])
    qtype = HiddenField(validators=[Required('')],default="radio")
    qtn_mark = HiddenField(validators=[Required('')],default=1)
    option = FieldList(FormField(QuestionOptionForm), min_entries=4)
    submit = SubmitField("create")

class PassQuizForm(Form):
    answers = FieldList(FormField(QuestionOptionForm))
    submit = SubmitField("create")
