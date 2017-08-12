# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from passlib.hash import sha256_crypt
from functools import wraps
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db, mysql

# Import module forms
from app.authentication.forms import RegisterForm

# Import module models (i.e. User)
from app.authentication.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
authentication = Blueprint('authentication', __name__, url_prefix='/auth')
# Set the route and accepted methods
@authentication.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form) #and form.validate():
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        #name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
       # cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
        
        cur.execute("INSERT INTO user(first_name, last_name, email, username, password) VALUES(%s, %s, %s, %s, %s)", (first_name, last_name, email, username, password))


        # Commit to DB
        mysql.connection.commit()
        print "Registered"

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect('/auth/login')
    return render_template('authentication/register.html', form=form)

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect('dashboard')
            else:
                error = 'Invalid login'
                return render_template('authentication/login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('authentication/login.html', error=error)

    return render_template('authentication/login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@authentication.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))
   

@authentication.route('/signin/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("authentication/signin.html", form=form)