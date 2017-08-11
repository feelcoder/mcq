# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash


# Import the database object from the main app module
from sqlalchemy.orm import Session

# Define the blueprint: 'auth', set its url prefix: app.url/auth
stat = Blueprint('stat', __name__, url_prefix='/stat')


from app import db, statistic
from app.authentication.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
statistic = Blueprint('statistic', __name__, url_prefix='/stat')

# Set the route and accepted methods
@statistic.route('/statistic',methods=['GET','POST'])
def statResult():

    db.create_all()
    users = User.query.all()

    for temp in users:
        print temp.id
    return render_template('statistic/statistic.html', users=users)

