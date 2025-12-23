from pprint import pprint

import requests
import boto3


url = 'https://armyinform.com.ua/wp-content/uploads/2025/12/armiya-tv_udary-po-naftovij-platformi.jpg'

# response = requests.get(url=url)
# print(response.content)
# with open('s3_practice/platformi.jpg', mode='bw') as file:
#     file.write(response.content)

# with open('s3_practice/platformi.jpg', mode='br') as file:
#     print(file.read())

# with open('s3_practice/platformi.jpg', mode='ba') as file:
#     file.write(b' hello there')


BUCKET_NAME = 'group11112025'
PUBLIC_URL ='https://pub-f8a0a61d58744db88283773e03043bb4.r2.dev'

s3 = boto3.client(
    "s3",
    region_name="EEUR",
    endpoint_url="https://8721af4803f2c3c631a90d8b64d397b7.r2.cloudflarestorage.com",
    aws_access_key_id="2ae25d402a48e45a66e8400661cb1e8f",
    aws_secret_access_key="32d65a0b27b9fb3789484262804a790c877a1257d96831a197f2cb182b616bdd",
)

# UPLOAD FILE
target_filename = 'images/spring12355.jpeg'
s3.upload_file('s3_practice/platformi.jpg', BUCKET_NAME, target_filename)
maybe_url = f'{PUBLIC_URL}/{target_filename}'
print(maybe_url)

# LIST OF FILES

# response = s3.list_objects_v2(Bucket=BUCKET_NAME)
# pprint(response)

# DOWNLOAD
# s3.download_file(BUCKET_NAME, target_filename, 's3_practice/5555.jpg')
