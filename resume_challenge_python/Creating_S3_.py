import boto3
from botocore.exceptions import NoCredentialsError

def create_s3_bucket(bucket_name, region='us-east-1'):
    try:
        # Create an S3 client
        s3 = boto3.client('s3', region_name=region)

        # Create a new S3 bucket
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )

        print(f"Bucket '{bucket_name}' created successfully in region '{region}'.")

    except NoCredentialsError:
        print("Credentials not available.")

if __name__ == "__main__":
    # Replace 'your-unique-bucket-name' with a globally unique name for your bucket
    bucket_name = 'mighur-s3-bucket'

    # Specify the AWS region where you want to create the bucket
    region = 'us-east-2'

    create_s3_bucket(bucket_name, region)
