import boto3
import json
s3 = boto3.client('s3')
bucket_name = 'mighur-s3-bucket'
bucket_policy = {
     'Version': '2012-10-17',
     'Statement': [{
         'Sid': 'AddPerm',
         'Effect': 'Allow',
         'Principal': 'IAM-ADMIN-USER',
         'Action': ['s3:GetObject'],
         'Resource': "arn:aws:s3:::mighur-s3-bucket" % bucket_name
      }]
 }
bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)