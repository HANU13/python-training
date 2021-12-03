import boto3
import json
#01. select ian role
iam=boto3.client("iam")
role=iam.get_role(RoleName="rl03dechanu")
print("---------")
print(role["Role"]["Arn"])
print("---------")
lambdaClient=boto3.client("lambda")

#02. create lambda.zip
dir_name=r"C:\practicals\Vodapythontrainingdec1todec3\serverlessarci"
output_file="lambda"
import shutil
shutil.make_archive(output_file,'zip',dir_name)
print("zip created kindly check...")

#03. convert lambda.zip into object
zipped_code=""
with open("lambda.zip","rb") as f:
    zipped_code=f.read()
print("----Zippedcode Created--------")

#04. create lambda fun using parameters
lambdaClient=boto3.client("lambda")
response=lambdaClient.create_function(
  FunctionName="fn03dechanuaaaa",
  Runtime="python3.8",
  Role=role["Role"]["Arn"],
  Handler="handler.lambda_handler",
  Code=dict(ZipFile=zipped_code),
  Timeout=300
)

print(response)