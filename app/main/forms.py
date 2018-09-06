from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    category = StringField('Category',validators=[Required()])
    pitch = TextAreaField('Your Pitch')
    submit = SubmitField('Submit')