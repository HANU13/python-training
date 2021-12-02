import boto3

ec2=boto3.resource("ec2")

KeyPairName="hanuk" #key - key-0cdb0d9751055f11f
imageId="ami-0ed9277fb7eb570c9"

instances=ec2.create_instances(
    MinCount=1,
    MaxCount=1,
    ImageId=imageId,
    InstanceType="t2.micro",
    KeyName=KeyPairName,
    TagSpecifications=[{
        "ResourceType":"instance",
        "Tags":[{
            "Key":"Name",
            
            "Value":"ITsHanu"
        }]
    }]
)

for instance in instances:
    print("Instance Created with id as: ",instance.id)

    instance.wait_until_running()
    print("Started")