import boto3
import logging

#logger config
logger=logging.getLogger()
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s: %(message)s')

vpcClient=boto3.client("ec2",region_name="ap-northeast-1") #vpc-0ada29c375918795b  #0b6e5e00a25e3bc9a

def fnVPCDelete(vpcId):
    from botocore.exceptions import ClientError
    vpc=None
    try:
        vpc=vpcClient.delete_vpc(VpcId=vpcId)
        logger.info("Listing vpc done")
    except ClientError as ce:
        print("Found error",ce)
        logger.exception("not posssible")
    return vpc

#driver code- workflow
if __name__=="__main__":
    vpc=fnVPCDelete(vpcId="vpc-0b6e5e00a25e3bc9a")
    print("deleted")
