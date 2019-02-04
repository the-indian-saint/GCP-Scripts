import os
import csv
import time
import json


with open ('deletevpc.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    for values in data:
        projectId = values['ProjectID']
        list_vpc = "gcloud compute networks delete default -q"
        prj_command = "gcloud config set project %s" %(projectId)
        os.system(prj_command)
        firewall_command = "gcloud compute firewall-rules list --format=json > firewalls.json"
        os.system(firewall_command)
        with open ('firewalls.json', 'r') as jsonfile:
            data2 = json.load(jsonfile)
            for network in data2:
                firewall_rule = network['name']
                #print(firewall_rule)
                condi = "https://www.googleapis.com/compute/v1/projects/%s/global/networks/default" %(projectId)
                if network['network'] == condi:
                    command3 = "gcloud compute firewall-rules delete %s -q" %(firewall_rule)
                    os.system(command3)
                    # os.remove('firewalls.json')
        os.system(list_vpc)
