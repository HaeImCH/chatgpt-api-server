from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
import json

with open('./settings.json', 'r',encoding="utf-8") as f:
    settings = json.load(f)

class FormAccessToken(FlaskForm):
    api_key = StringField(settings['text']['api_key'], validators=[DataRequired()], description=settings['text']['api_key_desc'])
    email = StringField(settings['text']['FromAccessToken']['email'], validators=[DataRequired()], description=settings['text']['FromAccessToken']['email_desc'])
    password = PasswordField(settings['text']['FromAccessToken']['password'], validators=[DataRequired()], description=settings['text']['FromAccessToken']['password_desc'])
    submit = SubmitField(settings['text']['submit'])