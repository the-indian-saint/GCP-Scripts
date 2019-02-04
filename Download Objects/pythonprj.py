from googleapiclient import discovery
from oauth2client.client import GoogleCredentials



credentials = GoogleCredentials.get_application_default()
service = discovery.build('cloudresourcemanager', 'v2', credentials=credentials)
project_body = {
                'name':'sindhuapifolder123',
                'displayName':'sindhuapifolder',
                'parent':'organizations/670075941769'
            }
request = service.folders().create(body=project_body)
request.execute()
print(request)
