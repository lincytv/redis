import boto3
import os
import sys
#light_box_id = "2CEA5884-4246-498E-A26D-F7C10D4034FE"
light_box_id = "49F68389-500C-41D5-96A8-4E183B14BE82"
table_name = "lightbox_content"
##############################################################
client = boto3.client("dynamodb", "eu-west-1")
resource = boto3.resource("dynamodb", "eu-west-1")
#####
#paginator = boto3.get_paginator('scan')
scaner = client.scan(TableName="lightbox_content")
f = open("reff.txt", "r+")
for ref_id in f:
    print(ref_id)
    for i in scaner["Items"]:
        lid = str(i['LighboxId']).split("'")
        a1 = lid[3].split("{")
        a = a1[1].split("}")
        print(lid[3])
        if a[0] == light_box_id:
        #if lid[3] == light_box_id:
            x = str(i["Ref"]).split("'")
            b1 = x[3].split("{")
            if b1[0] == ref_id:
                print(a[0], b1[0])
                # de = client.delete_item(
                #     TableName="lightbox_content",
                #     Key={
                #         'LightboxId': a[0],
                #          'Ref' : b1[0]
                #         }
                # )
                # print(de+"Deleted")