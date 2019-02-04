from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()


bucket_name = raw_input("Provide bucket name ")
projectId = raw_input("Provide the project Id ")
location = raw_input("Provide the location for %s " %(bucket_name))


request_body = {}
request_body['name'] = bucket_name
request_body['location'] = location


service = discovery.build('storage','v1',credentials=credentials)
request = service.buckets().insert(project=projectId, body=request_body)
request.execute()






