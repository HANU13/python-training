import boto3

vpcResource=boto3.resource("ec2",region_name="ap-northeast-1")
groupName="sgsample"
vpcId="vpc-03f15ca31abb556f1"
response=vpcResource.create_security_group(
    Description="creating for demo purpose",
    GroupName=groupName,
    VpcId=vpcId,
    TagSpecifications=[{
        "ResourceType":"security-group",
        "Tags":[{'Key':'Name','Value':groupName}]
    }]
    )

print(response.id)#sg-0fbe0492a89ca88e7