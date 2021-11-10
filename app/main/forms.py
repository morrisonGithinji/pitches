from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField, validators
from wtforms.validators import InputRequired
from ..models import Pitch, Comment

class PitchForm(FlaskForm):
    category = SelectField('Category', choices = [('Job','Job'),('Pick-up','Pick-up'),('Band','Band'),('Business','Business')], validators = [InputRequired()])
    title = StringField('Pitch title',validators=[InputRequired()])
    pitch = TextAreaField('Pitch', )
    submit = SubmitField('Submit')
    
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit') 
    
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a commment', validators=[InputRequired()])
    submit = SubmitField('Add')             