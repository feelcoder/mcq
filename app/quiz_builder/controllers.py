# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.quiz_builder.forms import QuizAddForm, QuestionForm
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
    return render_template("quiz_builder/quizview.html", quiz=currentQuiz)


@quiz.route('/<id>/question/add', methods=['GET', 'POST'])
def questionAdd(id):
    form = QuestionForm(request.form)
    if form.validate_on_submit():
        # build question tables
        qtn_text = form.text.data
        qtn_type = form.type.data
        qtn_mark = form.qtn_mark.data
        question = Question(qtn_text, qtn_type, qtn_mark)
        db.session.add(question)
        db.session.commit()
        if question.id:
            print("the type of form qnts options is %s " %
                  type(form.qtn_options.data))
    
    return redirect('/home')
