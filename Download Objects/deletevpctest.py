from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute','v1',credentials=credentials)
request = service.networks().delete(project='kunwarlimtd', network='default')
response = request.execute()
print("The output is --- ",response)
