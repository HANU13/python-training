import boto3
vpcClient=boto3.client("ec2",region_name="ap-northeast-1") #vpc-0ada29c375918795b

def fnVPCDescribe(tagKey,tagValues,maxItems=5):
    from botocore.exceptions import ClientError
    vpcLists=[]
    try:
        paginator=vpcClient.get_paginator("describe_vpcs")
        response_iterator=paginator.paginate(Filters=[
            {'Name':f'tag:{tagKey}',
             'Values':tagValues
            }
            ],PaginationConfig={'MaxItems':maxItems})
        full_result=response_iterator.build_full_result()
        for page in full_result["Vpcs"]:
            vpcLists.append(page)
        print("Listing vpc done")
    except ClientError as ce:
        print("Found error",ce)
    return vpcLists

#driver code- workflow
if __name__=="__main__":
    vpcLists=fnVPCDescribe(tagKey="Name",tagValues=["hanu"],maxItems=10)
    for vpc in vpcLists:
        print( vpc )
