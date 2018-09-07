from flask import render_template
from flask_login import login_required
from . import main
from .forms import PitchForm
from ..models import Pitch
from ..auth.forms import RegistrationForm

@main.route('/')
def index():
    '''
    function that returns index and its content
    '''
    form = RegistrationForm()
    return render_template('index.html', registration_form = form)

@main.route('/pitch')
def home():
    '''
    function that returns root.html page and its content
    '''
    title = 'Home'
    return render_template('root.html', title = title)

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


