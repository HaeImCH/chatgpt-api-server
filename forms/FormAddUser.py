from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import json

with open('./settings.json', 'r',encoding="utf-8") as f:
    settings = json.load(f)

class FormAddUser(FlaskForm):
    plus = SelectField(label=settings['text']['FormAddUser']['plus'], validators=[DataRequired()], choices=[('true', settings['text']['true']), ('false', settings['text']['false'])], default='false', description=settings['text']['FormAddUser']['plus_desc'])
    is_client = SelectField(label=settings['text']['FormAddUser']['is_client'], validators=[DataRequired()], choices=[('true', settings['text']['true']), ('false', settings['text']['false'])], default='false', description=settings['text']['FormAddUser']['is_client_desc'])
    userid = StringField(settings['text']['FormAddUser']['userid'], validators=[DataRequired()], description=settings['text']['FormAddUser']['userid_desc'])
    username = StringField(settings['text']['FormAddUser']['username'], validators=[DataRequired()], description=settings['text']['FormAddUser']['username_desc'])
    submit = SubmitField(settings['text']['submit'])