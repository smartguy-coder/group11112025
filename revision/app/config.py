import os
from dotenv import load_dotenv
import logging

load_dotenv()

BETTERSTACK_TOKEN = os.getenv('BETTERSTACK_TOKEN', 'N8jPPLhPSAWbhDAueTZhvKmf')
BETTERSTACK_HOST = os.getenv('BETTERSTACK_HOST')
LOG_LEVEL = logging.DEBUG

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_USERNAME = os.getenv("REDIS_USERNAME")
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')


JWT_SECRET = os.getenv('JWT_SECRET')

