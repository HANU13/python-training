import boto3
import os
s3=boto3.client("s3")

AWS_REGION=os.environ["RC"]
print("You Passed RC ac :",AWS_REGION)

bucketName="bkt01hanu"
location={'LocationConstraint':AWS_REGION}

#response=s3.create_bucket(Bucket=bucketName,CreateBucketConfiguration=location)
response=s3.create_bucket(Bucket=bucketName)
print("check with : aws s3 ls")
