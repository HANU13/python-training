import boto3

def fnCreateDefaultVPC(vpcClient):
    from botocore.exceptions import ClientError
    try:
        response=vpcclient.create_default_vpc()
        vpcId=response["Vpv"]["VpcId"]
        print("create default vpc")
    except ClientError:
        print("not possible to create")

#driver code- workflow
if __name__=="__main__":
    vpcclient=boto3.client("ec2")
    vpcId=fnCreateDefaultVPC(vpcclient)
    print( vpcId )



