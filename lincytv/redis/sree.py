import boto3
import os
region = "eu-west-1"
conn = boto3.client("dynamodb", region)
light_box_id = "2CEA5884-4246-498E-A26D-F7C10D4034FE"

f = open("reff.txt", "r+")
for i in f:
    print(i)
    read_data = conn.get_item(
        TableName= 'lightbox_content',
        Key={
            'LighboxId':{
                'S': light_box_id
            }
        }
    )
    print read_data

    # read_db = conn.delete_item(
    #     TableName='lightbox_content',
    #     Key={
    #         'LighboxId': {
    #             'S': light_box_id,
    #         },
    #         'Ref': {
    #             'S': i,
    #         },
    #     }
    # )
    # print("Deleated"+read_db)
