import os
import cgi
import json
import time
import yaml
import cgitb
import base64
import requests
import multiprocessing
from urllib.parse import unquote
from bson.json_util import dumps
from bson.objectid import ObjectId
from googleapiclient import discovery
from oauth2client.file import Storage
from requests_oauthlib import OAuth2Session
from oauth2client.client import OAuth2WebServerFlow
# Local Imports
import utils
from settings import *
def cluster_deletion(project, username, cluster_id):
    """
    Function Name : cluster_deletion
    Purpose       : This function deletes a GCP cluster
    Arguments     : project, username, cluster_id
    Returns       : status
    """
    try:
        cluster = db_orchestration.user_gcp_cluster.find_one(
            {"_id": ObjectId(cluster_id), "status": 0})
        if cluster:
            gcp_project_id = cluster["gcp_cluster_data"]["projectid"]
            zone = cluster["gcp_cluster_data"]["zone"]
            cluster_name = cluster["gcp_cluster_data"]["clustername"]
            credentials_file = "/opt/projects/" + username + "/Orchestration" + "/" + project + "/gcp/saas/credentials"
            log_file_path = "/opt/projects/" + username + "/Orchestration" + "/" + project + "/" + gcp_project_id + "/gcp/saas/logs"
            storage = Storage(credentials_file)
            credentials = storage.get()
            service = discovery.build('container', 'v1',
                                      credentials=credentials)
            request = service.projects().zones().clusters().delete(
                projectId=gcp_project_id,
                zone=zone,
                clusterId=cluster_name)
            response = request.execute()
    except Exception as e:
        output = json.dumps({'message': e.__str__()})
        utils.write_log(log_file_path, "deletion_log", output)
        print(output)
    else:
        if response['status'] == "RUNNING":
            delete_gcp_cluster = db_orchestration.user_gcp_cluster.update(
                {"_id": ObjectId(cluster_id)},
                {"$set": {"operation_id": response['name'],
                          "operationType": response['operationType'],
                          "launch_cluster_status": response['status'],
                          "status": 2}})
            output = json.dumps({'message': response['status']})
            utils.write_log(log_file_path, "deletion_log", response)
            print(output)
            status_process = multiprocessing.Process(target=check_status, args=(
            service, gcp_project_id, zone, response['name'],
            ObjectId(cluster_id)))
            status_process.start()
            # check_status(service, project_id, zone, response['name'], ObjectId(cluster_id))
        else:
            output = json.dumps({'message': response['status']})
            utils.write_log(log_file_path, "deletion_log", response)
            print(output)
