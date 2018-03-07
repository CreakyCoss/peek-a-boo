from . import main
from flask import url_for, render_template


@main.route('/')
def index():
    return render_template('index.html')
