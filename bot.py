import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

print(username)
print(password)