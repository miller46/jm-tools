import boto3
from botocore.exceptions import NoCredentialsError


class S3():

    @staticmethod
    def upload(local_file, bucket, s3_file, recursive=False):
        s3 = boto3.client('s3')
        try:
            s3.upload_file(local_file, bucket, s3_file)
            print(f"Upload Successful: {local_file} to {bucket}/{s3_file}")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    @staticmethod
    def download_from_s3(s3_file, bucket, local_file, recursive=False):
        s3 = boto3.client('s3')
        try:
            s3.download_file(bucket, s3_file, local_file)
            print(f"Download Successful: {s3_file} from {bucket} to {local_file}")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False
