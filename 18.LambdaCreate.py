import boto3
import json

iam=boto3.client("iam")


role=iam.get_role(RoleName="rl03dechanu")
print("---------")
print(role["Role"]["Arn"])
print("---------")
lambdaClient=boto3.client("lambda")
zipped_code=""
with open("lambda.zip","rb") as f:
    zipped_code=f.read()
print("----Zippedcode Created--------")
response=lambdaClient.create_function(
  FunctionName="fn03dechanuaa",
  Runtime="python3.8",
  Role=role["Role"]["Arn"],
  Handler="handler.lambda_handler",
  Code=dict(ZipFile=zipped_code),
  Timeout=300
)

print(response)