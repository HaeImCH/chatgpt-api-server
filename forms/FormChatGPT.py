from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
import json
with open('./settings.json', 'r',encoding="utf-8") as f:
    settings = json.load(f)

class FormChatGPT(FlaskForm):
    api_key = StringField(settings['text']['api_key'], validators=[DataRequired()], description=settings['text']['api_key_desc'])    
    prompt = TextAreaField(settings['text']['FormChatGPT']['prompt'], validators=[DataRequired()])
    conversation_id = StringField(settings['text']['conversation_id'], description=settings['text']['FormChatGPT']['conversation_id_desc'])
    plus = SelectField(label=settings['text']['FormChatGPT']['plus'], choices=[('any', settings['text']['FormChatGPT']['plus_any']), ('true', settings['text']['FormChatGPT']['plus_true']), ('false', settings['text']['FormChatGPT']['plus_false'])], default='false', description=settings['text']['FormChatGPT']['plus_desc'])
    reply_only = SelectField(settings['text']['FormChatGPT']['reply_only'], description=settings['text']['FormChatGPT']['reply_only_desc'], choices=[('false', settings['text']['false']), ('true', settings['text']['true'])], default='false')
    pretty = SelectField(settings['text']['FormChatGPT']['pretty'], description=settings['text']['FormChatGPT']['reply_only_desc'], choices=[('false', settings['text']['false']), ('true', settings['text']['true'])], default='true')    
    access_token = StringField(settings['text']['FormChatGPT']['access_token'], description=settings['text']['FormChatGPT']['access_token_desc'])
    user_plus = SelectField(label=settings['text']['FormChatGPT']['user_plus'], choices=[('true', settings['text']['true']), ('false', settings['text']['false'])], default='false', description=settings['text']['FormChatGPT']['user_plus_desc'])
    submit = SubmitField(settings['text']['submit'])