
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

# CREATE

# strings
redis_client.set('myKey', 'stored data')
redis_client.set('myKeyTTL', 'stored data', ex=15)
redis_client.set('myKeyTTL_sharp_date', 'stored data', exat=datetime.datetime(year=2026, month=1, day=1, hour=3, minute=6))
redis_client.set('myKey', 'stored data66666666666666666666666')

# list
# redis_client.lpush('list-key', 'init value')
redis_client.lpush('list-key', 'second value')
redis_client.rpush('list-key', 'third value', 'hhh', *['uuuuuu', 'rrrrrrr'])
redis_client.expire('list-key', 10666)

# dict
redis_client.hset('user:1234', mapping={'name': "Alize", "age": 26})
redis_client.hset('user:1234', mapping={'address': 'Odesa'})
redis_client.hset('user:1234', mapping={'address': 'Poltava'})
redis_client.expire('user:1234', 1000)

# READ

# strings
# my_value_str = redis_client.get('myKeyTTL_sharp_date')
# print(my_value_str)

# lists
data_from_list = redis_client.lrange('list-key', 0, -1)
# print(data_from_list)

# dict
data_from_dict = redis_client.hgetall('user:1234')
# print(data_from_dict)


# DELETE
# redis_client.delete('list-key', 'user:1234')
