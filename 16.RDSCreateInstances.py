import boto3

rds=boto3.client("rds")

response=rds.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    DBInstanceIdentifier="dbhanu",
    Engine="MySQL",
    MasterUserPassword="pass01admin",
    MasterUsername="admin01"
)

print(response)