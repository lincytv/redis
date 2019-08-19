import boto3
import os
import sys
dynamodb = boto3.resource('dynamodb', region_name="eu-west-1" )
light_box_id = "{9F68389-500C-41D5-96A8-4E183B14BE82}"
table = dynamodb.Table('lightbox_content')
response = table.scan()
data = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    #print response['Items']
    f = open("reff.txt", "r+")
    for ref_id in f:
        for i in response["Items"]:
            lid = str(i["LighboxId"]).split("'")
            lig_id = str(lid).split("'")
            #print type(i["Ref"])
            reff_id = str(i["Ref"]).rstrip()
            if lig_id[1] == light_box_id:
                if reff_id == ref_id:
                    print(i["Ref"])
                    print(lig_id[1])
                    # de = dynamodb.delete_item(
                    #     TableName="lightbox_content",
                    #     Key={
                    #         'LightboxId': lig_id[1],
                    #          'Ref' : ref_id
                    #         }
                    # )
                    # print(de+"Deleted")