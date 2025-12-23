import requests

url = 'https://armyinform.com.ua/wp-content/uploads/2025/12/armiya-tv_udary-po-naftovij-platformi.jpg'

response = requests.get(url=url)
# print(response.content)
# with open('s3_practice/platformi.jpg', mode='bw') as file:
#     file.write(response.content)

# with open('s3_practice/platformi.jpg', mode='br') as file:
#     print(file.read())

# with open('s3_practice/platformi.jpg', mode='ba') as file:
#     file.write(b' hello there')

import boto3
from botocore.config import Config

s3 = boto3.client(
    "s3",
    region_name="us-east-1",
    endpoint_url="https://objstorage.leapcell.io",
    aws_access_key_id="cb67e4bbfcfa4d10ba3ac6a4623f0c8a",
    aws_secret_access_key="1e8d341be3ed5ce625a0d24ede4c3fe92e2f8a3c6511f07c9a87a556dc838b83",
    config=Config(
        signature_version='s3v4',
        s3={'addressing_style': 'virtual'}  # або 'virtual'
    )
)



# List files
response = s3.list_objects_v2(Bucket="test1-pc5o-swmd-ahdtsabh")
for obj in response.get("Contents", []):
    print(obj["Key"])

# # Upload a file
# s3.put_object(
#     Bucket="test1-pc5o-swmd-ahdtsabh",
#     Key="example11.txt",
#     Body="Hello, this is a sample file content."
# )
#
# # Download a file
# response = s3.get_object(
#     Bucket="test1-pc5o-swmd-ahdtsabh",
#     Key="example.txt"
# )
# content = response["Body"].read().decode("utf-8")
# print("Downloaded content:", content)
#
# # Delete files
# s3.delete_objects(
#     Bucket="test1-pc5o-swmd-ahdtsabh",
#     Delete={
#         "Objects": [
#             {"Key": "example.txt"},
#             {"Key": "another_file.txt"}
#         ]
#     }
# )
