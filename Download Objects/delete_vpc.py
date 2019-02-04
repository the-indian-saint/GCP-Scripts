from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

#SCOPES = ['https://www.googleapis.com/auth/cloud-billing']
#SERVICE_ACCOUNT_FILE = '/Users/sindhuthudi/Downloads/'
#credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
credentials = GoogleCredentials.get_application_default()

proj_id = 'veenalimtd'

def delete_firewall(proj):
    service = discovery.build('compute', 'v1',credentials=credentials)
    request1 = service.firewalls().list(project=proj)
    response1 = request1.execute()
    #print(response1)
    for firewall in response1['items']:
        #print(firewall['network'])
        #fw_network = "https://www.googleapis.com/compute/v1/projects/%s/global/networks/default" %(proj)
        #if firewall['network'] == "fw_network":
            #print("In firewall if")
        request2 = service.firewalls().delete(project=proj,firewall=firewall['name'])
        response2 = request2.execute()
        print(response2)
    
    

def list_firewall(proj):
    
    service = discovery.build('compute', 'v1',credentials=credentials)
    firewalls_to_list= service.firewalls().list(project=proj)
    firewalls = firewalls_to_list.execute()
    for firewall in firewalls['items']:
        print(firewall['name'])
    
    for firewall in firewalls['items']:
        if firewall['network'] == 'default':
			firewall_to_delete = firewall['name']
			delete_firewall(firewall_to_delete,proj)



def delete_networks(proj):
    service = discovery.build('compute', 'v1', credentials=credentials)
    networks_to_delete= service.networks().delete(project=proj,network="default")
    response = networks_to_delete.execute()
    print(response)
    


#delete_firewall(proj_id)
delete_networks(proj_id)
