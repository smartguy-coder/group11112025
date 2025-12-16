
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

pubsub = redis_client.pubsub()
pubsub.subscribe('weather')
pubsub.subscribe('school')
pubsub.subscribe('abc')
pubsub.subscribe('*')

for message in pubsub.listen():
    print(message)
