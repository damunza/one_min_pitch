from flask import render_template
from flask_login import login_required
from . import main
from .forms import PitchForm, CommentForm
from ..models import Pitch, Comment
from ..auth.forms import RegistrationForm

@main.route('/')
def index():
    '''
    function that returns index and its content
    '''
    form = RegistrationForm()
    return render_template('index.html', registration_form = form)

@main.route('/root')
def home():
    '''
    function that returns root.html page and its content
    '''
    title = 'Home'
    return render_template('comment.html', title = title)

@main.route('/pitch/<cat>')
def category(cat):
    '''
    function to return the pitches
    '''
    category = Pitch.get_pitch(cat)
    print(category)
    title = f'{cat}'
    return render_template('pitch.html',title = title, category = category)

@main.route('/new-pitch',methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        cat = form.category.data
        pich = form.pitch.data

        new_pitch = Pitch(category = cat, pitch = pich)

        new_pitch.save_pitch()

    title = 'New Pitch'
    return render_template('new_pitch.html', title=title, pitch_form = form)

@main.route('/comment')
def comment():
    '''
    function to return the pitches
    '''
    comment = Comment.get_comment()
    print(comment)
    title = 'comments'
    return render_template('root.html',title = title, comment = comment)

@main.route('/new_comment', methods = ['GET', 'POST'])
def new_comment():
    form = CommentForm()

    if form.validate_on_submit():
        writer = form.author.data
        com = form.comment.data

        new_comment = Comment(comment = com, author = writer)
        new_comment.save_comment()

    title = 'New Comment'
    return render_template('new_comment.html', title = title, comment_form = form)
