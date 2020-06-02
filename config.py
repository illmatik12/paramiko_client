"""Remote host configuration."""
from os import environ, path
from dotenv import load_dotenv

# Load environment variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# Read environment variables
host = environ.get('REMOTE_HOST')
port = environ.get('REMOTE_PORT')
user = environ.get('REMOTE_USER')
pwd = environ.get('REMOTE_PASSWORD')

# 
api_server = environ.get('TELEGRAM_SERVER')
api_path = environ.get('TELEGRAM_PATH')
