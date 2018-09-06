from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    function that returns index and its content
    '''
    return render_template('index.html')