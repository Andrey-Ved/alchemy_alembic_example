import os

from dotenv import load_dotenv


load_dotenv()

DATABASE_NAME = os.getenv('DATABASE_NAME')

DATABASE_VARIANT = 0  # 0 or 1, or 2