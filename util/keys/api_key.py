import os

def get_openai_apikey():
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    return openai_api_key