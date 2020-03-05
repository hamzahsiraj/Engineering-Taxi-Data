import boto3   #install boto3 using pip
from config import ACCESS_KEY, SECRET_KEY    #config is the py file where the access keys are stored

s3 = boto3.client("s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
bucket_resource = s3
bucket_resource.upload_file(Bucket='bucket-name', Filename='pathToLocalFile', Key='desiredName.extension')
