from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import json
import subprocess as sp
import os
import sys

credentials = GoogleCredentials.get_application_default()
project = raw_input("Provide a name for the project: ")
input1 = raw_input("Type 'o' to create %s inside an Organization or type 'f' to create it inside a folder " %(project))


if input1.lower() == 'o':
    parent = raw_input("Provide the Organization ID ")
    parent_type = 'organizations/' + parent
elif input1.lower() == 'f':
    parent = raw_input("Provide the Folder ID ")
    parent_type = 'folders/' + parent
billing_acc = raw_input("Provide billing account id ")

parent_body = {}
parent_body['id'] = parent
parent_body['type'] = parent_type
body = {}
#body['parent'] = parent_type
body['name'] = project
projectId = project + '-' + str(243221)
body['projectId'] = projectId
#project_body = json.dumps(body)

service = discovery.build('cloudresourcemanager','v1', credentials=credentials)
request = service.projects().create(body=body)
while request is not None:
    request.execute()

command = "gcloud alpha billing projects link %s --billing-account %s" %(projectId, billing_acc)
os.system(command)

service2 = discovery.build('compute','v1', credetials=credentials)
request2 = service2.networks().delete(project=projectId, name='default')
while request2 is not None:
    request2.execute()

