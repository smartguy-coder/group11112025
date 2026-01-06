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


PGHOST = os.getenv('PGHOST')
PGDATABASE = os.getenv('PGDATABASE')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')



# rabbit
RMQ_PORT = os.getenv('RMQ_PORT')
RMQ_USER = os.getenv('RMQ_USER')
RMQ_VIRTUAL_HOST = os.getenv('RMQ_VIRTUAL_HOST')
RMQ_HOST = os.getenv('RMQ_HOST')
RMQ_PASSWORD = os.getenv('RMQ_PASSWORD')


