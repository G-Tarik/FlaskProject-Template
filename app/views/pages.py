from flask import render_template, flash, Blueprint

blue_view = Blueprint('views', __name__)


@blue_view.route('/', methods = ['POST', 'GET'])
def index():
    info_message = 'Hello magic :-)'
    flash(info_message)
    return render_template('index.html')


@blue_view.route('/about')
def about():
    return render_template('about.html')

