import os
import boto3
from pathlib import Path


# Please do not share the below keys, or check into a respository. 
ACCESS_KEY = os.getenv('S3_ACCESS_KEY', '') # IAM access Key
SECRET_KEY = os.getenv('S3_SECRET_KEY', '') #"IAM access key secret

BUCKET = "aveva-parkour"
REGION = 'us-east-1'

s3client = boto3.client(
    's3',
    region_name = REGION,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    #aws_session_token=SESSION_TOKEN
)

for object in s3client.list_objects(Bucket=BUCKET)['Contents']:
    if str(object['Key']).startswith("part-0000"):
        #Download to User's Downloads directory
        s3client.download_file('aveva-parkour', object['Key'], str(Path.home()) + '\Downloads\\' + 'downloaded_' + object['Key'])

# Download a single s3 object to local directory:
# s3client.download_file(BUCKET, 'part-00000-snappy.parquet', str(Path.home()) + '\Downloads\\' + 'downloaded_part-00000-snappy.parquet')

msg = "Download Complete"
print(msg)