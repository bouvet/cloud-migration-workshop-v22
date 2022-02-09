import json
import boto3
import uuid

S3_CLIENT = boto3.resource('s3')
DYNAMODB_CLIENT = boto3.resource('dynamodb')

TABLE_NAME =
S3_BUCKET_NAME =

def lambda_handler(event, context):

    filename = event['Records'][0]['s3']['object']['key']
    file_conent = read_s3_file(filename)

    if type(file_conent) is list:
        for object in file_conent:
            write_to_dynamo_db(object)
    else:
        write_to_dynamo_db(file_conent)

    print(f"successfully written object to DynamoDB table: {TABLE_NAME}")


def read_s3_file(filename):
    try:
        file = S3_CLIENT.Object(S3_BUCKET_NAME, filename).get()
        file_conent = json.load(file["Body"])
        return file_conent

    except Exception as e:
        print(f"Could not read json file: {filename} from S3 bucket: {S3_BUCKET_NAME}, error message: {str(e)}")
        raise e

def write_to_dynamo_db(content):
    try:
        table = DYNAMODB_CLIENT.Table(TABLE_NAME)
        content["id"] = content.get("id", str(uuid.uuid4()))
        table.put_item(Item=content)

    except Exception as e:
        print(f"Could not write object: {str(content)} to table: {TABLE_NAME}, error message: {str(e)}")
        raise e

