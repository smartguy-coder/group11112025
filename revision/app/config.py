import os
from dotenv import load_dotenv
import logging

load_dotenv()

BETTERSTACK_TOKEN = os.getenv('BETTERSTACK_TOKEN', 'N8jPPLhPSAWbhDAueTZhvKmf')
BETTERSTACK_HOST = os.getenv('BETTERSTACK_HOST')
LOG_LEVEL = logging.DEBUG
