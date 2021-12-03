import boto3 

dynamodb=boto3.resource("dynamodb")

ks=[
    {
        "AttributeName":"Name",
        "KeyType":"HASH"
    },
    {
        "AttributeName":"Email",
        "KeyType":"RANGE"
    }

]

ad=[
    {
        "AttributeName":"Name",
        "AttributeType":"S"
    },
    {
        "AttributeName":"Email",
        "AttributeType":"S"
    }

]

pt={"ReadCapacityUnits":1,"WriteCapacityUnits":1}

table=dynamodb.create_table(
    TableName="hanu03dec",
    KeySchema=ks,
    AttributeDefinitions=ad,
    ProvisionedThroughput=pt
)
print("Table: ",table)