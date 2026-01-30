import os
from dotenv import load_dotenv

load_dotenv()  # baca file .env

TOKEN = os.getenv("TOKEN")
