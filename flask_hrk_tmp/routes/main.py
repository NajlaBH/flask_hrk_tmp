from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from flask_hrk_tmp.extensions import db
from flask_hrk_tmp.models import  User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/users')
@login_required
def users():
    if not current_user.admin:
        return redirect(url_for('main.index'))

    #users = User.query.filter_by(admin=False).all()
    users = User.query.all()

    context = {
        'users' : users
    }

    return render_template('users.html', **context)

@main.route('/promote/<int:user_id>')
@login_required
def promote(user_id):
    if not current_user.admin:
        return redirect(url_for('main.index'))

    user = User.query.get_or_404(user_id)

    #user.expert = True
    db.session.commit()

    return redirect(url_for('main.users'))
