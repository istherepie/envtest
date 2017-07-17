# imports
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Get .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Settings
HOSTNAME = os.environ.get('HOST')
PORT = os.environ.get('PORT')
UUID = os.environ.get('UUID')
HEINI =  os.environ.get('HEINI')