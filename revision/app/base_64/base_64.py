import base64

string = b'hello 88 ** - () '

encode = base64.b64encode(string)
print(encode)

decoded = base64.b64decode(encode)
print(decoded)
