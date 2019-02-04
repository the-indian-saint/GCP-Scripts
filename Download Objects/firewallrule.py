from googleapiclient import discovery
from google.oauth2 import service_account
import csv

SCOPES = ['https://www.googleapis.com/auth/cloud-billing']
#SERVICE_ACCOUNT_FILE = '/Users/kunwarluthera/Downloads/kunwar-first-service-acc.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)


proj_id = 'brave-watch-214012'

def create_firewall(req):
    
    service = discovery.build('compute', 'v1',credentials=credentials)
    firewalls_to_create= service.firewalls().insert(project=proj_id, body=req)
    firewalls_to_create.execute()


with open('firewalls.csv', 'r') as csv_file:
  dict_reader = csv.DictReader(csv_file)
  for row in dict_reader:
    #print(row)
    req = {"name": row['Name'],"direction": row['Type']}
  
    if row['Action'] == 'Deny':
        req['denied'] = [
    {
      "IPProtocol": row['Protocols'],
      "ports": [
        row['Port']
      ]
    }
  ]
    if row['Action'] == 'Allow':
        req['allowed'] =  [
    {
      "IPProtocol": row['Protocols'],
      "ports": [
        row['Port']
      ]
    }
  ]
    if row['Type'] == 'Egress':
        req["destinationRanges"]= [
    row['destinationRanges']
  ]
    if row['Type'] == 'Ingress':
        req["sourceRanges"]= [
    row['sourceRanges']
  ]
    #print(req)
    create_firewall(req)
