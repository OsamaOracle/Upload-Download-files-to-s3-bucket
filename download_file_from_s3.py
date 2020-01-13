import os
import boto3
from botocore.client import Config

ACCESS_KEY_ID = "AKIAV5WYHEBUWZ5J2ZX5"
ACCESS_SECRET_KEY = "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"
BUCKET_NAME = 'zabbixtemplate'

#initiate s3 resource
s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
# select bucket
BUCKET_NAME = s3.Bucket('zabbixtemplate')

# download file into current directory
for s3_object in BUCKET_NAME.objects.all():
    # Need to split s3_object.key into path and file name, else it will give error file not found.
    path, filename = os.path.split(s3_object.key)
    BUCKET_NAME.download_file(s3_object.key, filename)
    print(s3_object.key + " File Downloaded!")
