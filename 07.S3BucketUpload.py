#upload_file(file_name,bucket_name,object_name )              upload_fileobj()
import boto3    
import pathlib

BASE_DIR=pathlib.path(__file__).parent.resolve()
BUCKET_NAME="specifybucketname"
FILE_NAME="specifyfilename"
object_name=FILE_NAME
# can also change the object name

s3client=boto3.client("s3")

s3client.upload_file(r"pastebaseaddress",BUCKET_NAME,object_name)
print("file uploades")

