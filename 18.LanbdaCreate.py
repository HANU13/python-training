import boto3

iam=boto3.client("iam")



lambda=boto3.client("lambda")

response=lambda.create_alias()