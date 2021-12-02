import boto3
#1 client
#s3client=boto3.client("s3")
#s3client.delete_bucket(Bucket="bkt01hanu")
#print("bucket deleted")
#2 resource
#s3resource=boto3.resource("s3")
#Bucket=s3resource.Bucket("bkt01hanu")
#Bucket.delete()
#print("bucket deleted")
#3 by input
#s3resource=boto3.resource("s3")
#bucketName=input("enter bucket name to delete :")
#Bucket=s3resource.Bucket(bucketName)
#Bucket.delete()
#print("bucket deleted")
#4 
s3resource=boto3.resource("s3")
bucketName="BUCKETNAME"
Bucket=s3resource.Bucket(bucketName)

def cleanup_bucket_objects(myBucket):
    # delete all objects
    for obj in myBucket.objects.all():
        obj.delete()
    # if obj has ver delete ver with obj
    for objver in myBucket.object_versions.all():
        objver.delete()
# delete all obj from bucket
cleanup_bucket_objects(Bucket)
#delete an empty bucket
Bucket.delete()
