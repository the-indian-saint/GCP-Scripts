from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

vpc = {
        'project':'project/brave-watch-214012'
      }
credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)
request = service.networks().list(project='myapiprj7777-243221')
#networks = request().execute()
#networks = request.read()
#print(networks)
# print(request)
while request is not None:
    response = request.execute()

    for network in response['items']:
        # TODO: Change code below to process each `network` resource:
        print(network['name'])

    request = service.networks().list_next(previous_request=request, previous_response=response)
    #print(network)
