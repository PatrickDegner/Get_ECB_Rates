from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv('database')
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')