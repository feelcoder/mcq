from app import db
from app.authentication.models import Base
import random
import string

# Define a Quiz model


class Quiz(Base):

    __tablename__ = 'quiz'

    # user id
    uid = db.Column(db.String(45), nullable=True)
    # quiz title
    title = db.Column(db.String(200),  nullable=False)

    # quiz instructions
    instructions = db.Column(db.Text,  nullable=False)

    # quiz id
    quid = db.Column(db.String(45),  nullable=False, unique=True)

    # quiz time
    time = db.Column(db.Integer,  nullable=True)

    # quiz total_marks
    total_marks = db.Column(db.Integer,  nullable=True)

    # quiz closed
    closed = db.Column(db.Boolean,  nullable=True)
    # quiz start date
    start_date = db.Column(db.DateTime,  nullable=True)

    # New instance instantiation procedure
    def __init__(self, title, instructions, uid, time, start_date, total_marks, closed):

        self.title = title
        self.instructions = instructions
        self.uid = uid
        self.time = time
        self.start_date = start_date
        self.total_marks = total_marks
        self.closed = closed
        self.quid = ''.join(random.SystemRandom().choice(
            string.ascii_uppercase + string.digits) for _ in range(26))

    def __repr__(self):
        return '<Quiz %r>' % (self.title)


class Question(Base):

    __tablename__ = 'question'

    quid = db.Column(db.String(64), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    qtn_mark = db.Column(db.Integer, nullable=True)
    # New instance instantiation procedure

    def __init__(self,quid, qtype, qtext, qtn_mark):

        self.quid = quid
        self.type = qtype
        self.text = qtext
        self.qtn_mark = qtn_mark

    def __repr__(self):
        return '<Question %r>' % (self.text)


class QuestionOption(Base):

    __tablename__ = 'question_options'

    qtn_id = db.Column(db.String(64), nullable=False)
    answer = db.Column(db.Integer, nullable=True)
    text = db.Column(db.String(200), nullable=False)

    def __init__(self, qnt_id, answer, text):
        self.qtn_id = qnt_id
        self.answer = answer
        self.text = text

    def __repr__(self):
        return '<Question %r>' % (self.text)
