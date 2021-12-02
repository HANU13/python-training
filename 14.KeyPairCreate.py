import boto3

#ec2=boto3.resource("ec2")

#Key_pair=ec2.KeyPair("")

#print(Key_pair)

ec2=boto3.client("ec2")
myKeyName="hanuk"
response=ec2.create_key_pair(KeyName=myKeyName)
with open(myKeyName+".pem","w")as f:
    f.write(response["KeyMaterial"])
print(response)    