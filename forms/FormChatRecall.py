from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import json
with open('./settings.json', 'r',encoding="utf-8") as f:
    settings = json.load(f)

class FormChatRecall(FlaskForm):
    api_key = StringField(settings['text']['api_key'], validators=[DataRequired()], description=settings['text']['api_key_desc'])
    conversation_id = StringField(settings['text']['conversation_id'], description= settings['text']['FormChatGPT']['conversation_id_desc'])    
    submit = SubmitField(settings['text']['submit'])