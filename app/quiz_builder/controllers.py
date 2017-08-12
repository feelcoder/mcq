# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from inspect import getmembers
from pprint import pprint
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.quiz_builder.forms import QuizAddForm, QuestionForm, QuestionOptionForm, PassQuizForm
# Import module models (i.e. User)
from app.quiz_builder.models import Quiz, Question, QuestionOption

# Define the blueprint: 'auth', set its url prefix: app.url/auth
quiz = Blueprint('quiz', __name__, url_prefix='/quiz')
# Set the route and accepted methods


@quiz.route('/add', methods=['GET', 'POST'])
def quizform():

    # If sign in form is submitted
    form = QuizAddForm(request.form)
    if form.validate_on_submit():
        if form.closed.data == "pv":
            closed = 1
        else:
            closed = 0
        quiz = Quiz(form.title.data, form.instructions.data, form.uid.data,
                    form.time.data, form.start_date.data, form.total_marks.data, closed)
        db.session.add(quiz)
        db.session.commit()
        print(" the id is %s" % quiz.id)
        if quiz.id:
            flash('Quiz %s succesfully created' % quiz.title)
            return redirect("/quiz/view/" + str(quiz.id))

    return render_template("quiz_builder/quizadd.html", form=form)


@quiz.route('/view/<id>', methods=['GET'])
def viewQuiz(id):
    # get quiz from database
    
    currentQuiz = Quiz.query.filter_by(id=id).first()
    questions = Question.query.filter_by(quid=id).all()
    
    return render_template("quiz_builder/quizview.html", quiz=currentQuiz,questions=questions)


@quiz.route('/exams', methods=['GET', 'POST'])
def statResult():
    quiz = Quiz.query.filter_by(uid=1234).all()
    quizCount = Quiz.query.filter_by(uid=1234).count()
    return render_template('quiz/list.html', quiz=quiz, quizCount=quizCount) 

@quiz.route('/live/<id>', methods=['GET'])
def interview(id):
    # get quiz questions from database
    currentQuiz = Quiz.query.filter_by(id=id).first()
    questions = Question.query.filter_by(quid=id).all()
    for question in questions: 
        tmpOptions = QuestionOption.query.filter_by(qtn_id=question.id).all()
        question.options = tmpOptions
    return render_template("quiz/takeQuiz.html", quiz=currentQuiz, questions=questions)

@quiz.route('/<id>/question/add', methods=['GET', 'POST'], defaults={'qtn_id': None})
@quiz.route('/<id>/question/add/<qtn_id>', methods=['GET', 'POST'])
def questionAdd(id, qtn_id):
    form = QuestionForm(request.form)
    if request.method == 'GET' and qtn_id is not None:
        question = Question.query.filter_by(id=qtn_id).first()
        form.text.data = question.text
    
        # create a list of of entries
        questionOption = QuestionOption.query.filter_by(
            qtn_id=question.id).all()
        print(len(questionOption))
        for qtn_option in questionOption:
            new_option = form.option.append_entry();
            new_option.answer.data = qtn_option.answer
            new_option.text.data = qtn_option.text

      
    quiz = Quiz.query.filter_by(id=id).first()
    for entry in form.option.entries:
        print(type(entry))
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # build question tables
        # pprint(getmembers(form))
        qtn_text = form.text.data
        qtn_type = form.qtype.data
        qtn_mark = form.qtn_mark.data
        question = Question(quid=id, text=qtn_text,
                            type=qtn_type, qtn_mark=qtn_mark)
        db.session.add(question)
        db.session.commit()
        if question.id:
            for entry in form.option.entries:
                if entry.data['answer'] is True:
                    answer = 1
                else:
                    answer = 0
                if entry.data['text'] is not None:

                    option = QuestionOption(
                        question.id, answer, entry.data['text'])
                    db.session.add(option)
                else:
                    pass

            db.session.commit()
            return redirect("/quiz/view/" + str(id))
        else:
            return redirect("/home")

    return render_template("quiz_builder/quiz_question_add.html", form=form, quiz=quiz)
