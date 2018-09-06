from flask import render_template
from . import main
from .forms import PitchForm
from ..models import Pitch

@main.route('/')
def index():
    '''
    function that returns index and its content
    '''
    return render_template('index.html')

@main.route('/pitch', methods = ['GET','POST'])
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        cat = form.category.data
        pich = form.pitch.data

        new_pitch = Pitch(category = cat, pitch = pich)

        new_pitch.save_pitch()

    title = 'Pitches'
    return render_template('new_pitch.html', title = title,pitch_form = form)