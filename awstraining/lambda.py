import json
import helperS3
def lambda_handler(event, context):
    bucketName,objectName=helperS3.findBucketObjectNames(event)
    jsonData=helperS3.get_data_from_object(bucketName,objectName)
   
    print("___________________________________")
    result=helperS3.insertIntoDynamoDB(jsonData)
    print("Inserted: ",helperS3.DYNAMODB_TABLE)
    print("___________________________________")
    
    print(helperS3.DYNAMODB_TABLE)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
