#IMPORT BUILT-IN LIBRARIES
from datetime import date
import json
import os
import platform

#LOAD SETTINGS FROM SETTINGS.JSON
with open('./settings.json', 'r') as f:
    settings = json.load(f)

#SETUP API TERMINAL NAME
API_TERMINAL_NAME = os.environ.get("API_TERMINAL_NAME") or str(settings['api_server']['terminal_name'])

#NAME TERMINAL BASED ON OS BEFORE ANYTHING ELSE
if platform.system() == 'Windows':
    os.system(f'title {API_TERMINAL_NAME}')
else:
    os.system(f'echo -e "\033]0;{API_TERMINAL_NAME}\007"')

#CONTINUE IMPORTS

#IMPORT CONTRIBUTED-CODE LIBRARIES
from contrib.OpenAIAuth.Cloudflare import Cloudflare

#IMPORT CLASSES
from classes.ChatGPT import ChatGPT

#IMPORT HELPER FUNCTIONS
from helpers.General import generate_api_key, json_key_exists, add_json_key

#LOADS API USER DATABASE
with open('./users.json', 'r') as f:
    users = json.load(f)
API_KEYS = users['API_KEYS']

async def reload_users():
    """
    Reloads the API user database
    """
    global API_KEYS
    with open('./users.json', 'r') as f:
        users = json.load(f)
    API_KEYS = users['API_KEYS']

update_settings = False
#SET ADMIN API KEYS IF NOT PRESENT
if not json_key_exists(settings, 'api_server', 'admin_api_key'):                    #if admin_api_key is not present in settings.json
    add_json_key(settings, generate_api_key(), 'api_server', 'admin_api_key')       #add admin_api_key to settings.json
    update_settings = True
if not json_key_exists(settings, 'api_server', 'readonly_api_key'):                 #if readonly_api_key is not present in settings.json
    add_json_key(settings, generate_api_key(), 'api_server', 'readonly_api_key')    #add readonly_api_key to settings.json
    update_settings = True
if not json_key_exists(settings, 'api_server', 'readwrite_api_key'):                #if readwrite_api_key is not present in settings.json
    add_json_key(settings, generate_api_key(), 'api_server', 'readwrite_api_key')   #add readwrite_api_key to settings.json
    update_settings = True
if not json_key_exists(settings, 'api_server', 'app_secret'):                       #if admin_api_key is not present in settings.json
    add_json_key(settings, generate_api_key(), 'api_server', 'app_secret')          #add admin_api_key to settings.json
    update_settings = True
if update_settings:
    with open('./settings.json', 'w') as f:
        json.dump(settings, f, indent=4)
    with open('./settings.json', 'r') as f:
        settings = json.load(f)

#SETUP OPENAI API DEFAULTS
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL") or str(settings['openai']['base_url'])
OPENAI_ENDPOINT_CONVERSATION = os.environ.get("OPENAI_CONVERSATION_ENDPOINT") or str(settings['openai']['endpoints']['conversation'])
OPENAI_ENDPOINT_GEN_TITLE = os.environ.get("OPENAI_GEN_TITLE_ENDPOINT") or str(settings['openai']['endpoints']['gen_title'])
OPENAI_BASE_PROMPT = (
    f'You are ChatGPT, a large language model trained by OpenAI. Respond conversationally. Do not answer as the user. Current date: {str(date.today())}.\n\n'
    f'User: Hello\n'
    f'ChatGPT: Hello! How can I help you today? <|im_end|>\n\n\n'
)

#SETUP API DEFAULTS
API_ADMIN_KEY = settings['api_server']['admin_api_key']
API_READONLY_KEY = settings['api_server']['readonly_api_key']
API_READWRITE_KEY = settings['api_server']['readwrite_api_key']
API_DEFAULT_PROXY = settings['api_server']['default_proxy']
API_APP_SECRET = settings['api_server']['app_secret']
API_CF_CLEARANCE, API_USER_AGENT = Cloudflare(proxy=API_DEFAULT_PROXY).get_cf_cookies()
API_HOST = os.environ.get("API_HOST") or str(settings['api_server']['host'])
API_PORT = os.environ.get("API_PORT") or int(settings['api_server']['port'])
API_LOCAL_BASE_URL = f'http://{API_HOST}:{API_PORT}'
API_DEFAULT_PROMPT = (
    f'Say the following: You did not enter a prompt. URL should be http://<IP>:<PORT>/chat?prompt=<prompt>\n'
    f'Join us at https://discord.gg/lukium for the best source of AI resources and tools,'
    f'including free Stable Diffusion Servers running on dedicated RTX 3090 GPUs,'
    f'as well as a community of AI enthusiasts.'
)

#SETUP API ENDPOINT URL CONSTANS
BROWSER_ENDPOINTS = settings['api_server']['endpoints']['browser']
API_ENDPOINTS = settings['api_server']['endpoints']['api']

ENDPOINT_BROWSER_CHATGPT = BROWSER_ENDPOINTS['chatgpt']['url']
ENDPOINT_BROWSER_CHATRECALL = BROWSER_ENDPOINTS['chatrecall']['url']
ENDPOINT_BROWSER_ACCESS_TOKEN = BROWSER_ENDPOINTS['access_token']['url']
ENDPOINT_BROWSER_ADD_USER = BROWSER_ENDPOINTS['add_user']['url']

ENDPOINT_API_CHATGPT = API_ENDPOINTS['chatgpt']['url']
ENDPOINT_API_CHATRECALL = API_ENDPOINTS['chatrecall']['url']
ENDPOINT_API_ACCESS_TOKEN = API_ENDPOINTS['access_token']['url']