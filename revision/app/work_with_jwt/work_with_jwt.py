import jwt
import datetime
import time


import config


current_time = datetime.datetime.now(datetime.timezone.utc)

payload = {
    "username": "vasyl",
    'age': 18,

    "sub": '123',  # string!!!!!!!

    'iat': current_time,
    "exp": current_time + datetime.timedelta(seconds=5)
}

encoded_jwt = jwt.encode(
    payload=payload,
    key=config.JWT_SECRET,
    algorithm='HS256'
)
print(encoded_jwt)

time.sleep(6)

decode = jwt.decode(
    jwt=encoded_jwt,
    key=config.JWT_SECRET,
    algorithms=['HS256'],
    # options={'verify_signature': False}
)
print(decode)

