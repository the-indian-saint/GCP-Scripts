from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from pprint import pprint


project = "rohanprjapites123-243221"
#network = "4271197226894506273"

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

#request = service.firewalls().list(project=project)
#while request is not None:
#response = request.execute()
#for firewall in response['items']:
        # TODO: Change code below to process each `firewall` resource:
    #name = firewall['name']
    #firw = name[2:-1]
    #request2 = service.firewalls().delete(project=project, firewall=firw)
    #response2 = request.execute()
request = service.networks().list(project=project)
response = request.execute()

#while request is not None:
    #response = request.execute()

for network in response['items']:
    # TODO: Change code below to process each `network` resource:
    pprint(network['name'])
    #while request is not None:
        #response = request.execute()
    if network['name'] == "u'default'":
        request1 = service.networks().delete(project=project, network=network['name'])
        response1 = request1.execute()
        pprint(response1)
    #for network in response['items']:
        # TODO: Change code below to process each `network` resource:
       # pprint(network)
        #if network['name'] == u'default':
            #request1 = service.networks().delete(project=project, network=network['name']
            #request1.execute()
#request = service.networks().list_next(previous_request=request, previous_response=response)
