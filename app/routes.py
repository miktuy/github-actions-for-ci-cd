from flask import render_template

from app import application


@application.route('/about')
def about():
    return render_template('about.html', title='About', active_page='about')


@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='Home', active_page='home')
