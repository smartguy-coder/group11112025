
import redis
import config
import datetime

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)

while True:
    channel = input('enter channel')
    message = input('enter message')
    redis_client.publish(channel, message)