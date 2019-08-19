import boto3
import os
import sys
light_box_id_prod = "2CEA5884-4246-498E-A26D-F7C10D4034FE"
light_box_id = "0273237E-E176-49E7-B9A4-801A11B714A8"
ref_id_dev = "A5RPJE"
table_name = "lightbox_content"
##############################################################
client = boto3.client("dynamodb", "eu-west-1")
resource = boto3.resource("dynamodb", "eu-west-1")
#####
scaner = client.scan(TableName="lightbox_content")
f = open("reff.txt", "r+")
for ref_id in f:
    for i in scaner["Items"]:
        lid = str(i['LighboxId']).split("'")
        a1 = lid[3].split("{")
        a = a1[1].split("}")
        if a[0] == light_box_id :
            x = str(i["Ref"]).split("'")
            b1 = x[3].split("{")
            if b1[0] == ref_id_dev:
                print(a[0], b1[0])
                de = client.delete_item(
                    TableName="lightbox_content",
                    Key={
                        'LightboxId': a[0],
                         'Ref' : b1[0]
                        }
                )
                print(e+"Deleted")
