import boto3
#1
#s3=boto3.client("s3")
#response=s3.list_buckets()
#for b in response["Buckets"]:
#    print( b["Name"] ,end="")

    # if("bkt" in b["Name"]):
    #     print(b["Name"])
#2
s3=boto3.resource("s3")
iterator=s3.buckets.all()

for b in iterator:
    print(f"{b.name}",end=',')
