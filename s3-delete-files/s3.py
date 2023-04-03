import boto3

access_key = ""
secret_key = ""
bucket = ""
region = ""

session = boto3.Session(
    region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key
)
# s3_client = boto3.client(
#             's3',
#             region_name=region,
#             aws_access_key_id=access_key,
#             aws_secret_access_key=secret_key,
#             verify=False
#           )

s3 = session.resource("s3")
bucket = s3.Bucket("")
prefix = ""

response = bucket.delete_objects(
    Delete={
        "Objects": [
            {
                "Key": ""
            }
        ]
    }
)

print(response)
