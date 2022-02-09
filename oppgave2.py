import json
import boto3

dynamodb = boto3.resource('dynamodb')
TABLE_NAME =


def lambda_handler(event, context):
    parameter = event["pathParameters"]["id"]

    return query_table(parameter)


def query_table(parameter):
    try:
        table = dynamodb.Table(TABLE_NAME)
        response = table.get_item(Key={'id': parameter})

        return create_return_object(200, response['Item'])
    except KeyError as e:
        print(f"Could not find object with id: {parameter} in table: {TABLE_NAME}, error message: {str(e)}")
        return create_return_object(404, {"message": f"Could not find object with id: {parameter}"})

    except Exception as e:
        print(f"Could not find object with id: {parameter} in table: {TABLE_NAME}, error message: {str(e)}")
        return create_return_object(500, {"message": "Internal server error, see logs"})


def create_return_object(status_code, body):
    return {
        'statusCode': status_code,
        'body': json.dumps(body)
    }

