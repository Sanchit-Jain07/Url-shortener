from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

class UrlForm(FlaskForm):
    link = StringField('Enter your link!',validators=[DataRequired(), URL(message='Please enter a URL')])
    submit = SubmitField('Shorten!')