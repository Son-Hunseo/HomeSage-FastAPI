import yaml
import os

# for local
# def get_openai_apikey(file_path : str = "./secrets.yaml"):
#     with open(file_path, 'r') as file:
#         secrets = yaml.safe_load(file)
#         openai_api_key = secrets['openai_api_key']
#     return openai_api_key

def get_openai_apikey():
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    return openai_api_key