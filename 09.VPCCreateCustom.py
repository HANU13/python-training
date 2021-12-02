import boto3

def fnCreateCustomVPC(vpcResource,IpCidr):
    from botocore.exceptions import ClientError
    vpcId="not set"
    try:
        response=vpcResource.create_vpc(CidrBlock=IpCidr,
        InstanceTenancy="default",
        TagSpecifications=[{"ResourceType":"vpc","Tags":[{'Key':'Name','Value':'hanu'}]}]
        )
        vpcId=response.id
        print("create default vpc")
    except ClientError as ce:
        print("not possible to create",ce)
    return vpcId

#driver code- workflow
if __name__=="__main__":
    vpcresource=boto3.resource("ec2",region_name="ap-northeast-1") #vpc-0ada29c375918795b
    ip_cidr="192.168.0.0/26" 
    vpcId=fnCreateCustomVPC(vpcresource,ip_cidr)
    print( vpcId )
