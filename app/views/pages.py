from flask import render_template, flash, Blueprint
from app.models import db, Users

blue_view = Blueprint('views', __name__)


@blue_view.route('/', methods = ['POST', 'GET'])
def index():
    info_message = 'Hello magic :-)'
    flash(info_message)
    users = db.session.query(Users).all()
    return render_template('index.html', users=users)


@blue_view.route('/about')
def about():
    return render_template('about.html')

