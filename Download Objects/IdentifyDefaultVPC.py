import os
import subprocess as sp
import json


command1 = "gcloud projects list --format json > projects.json"
sp.call(command1, shell=True)

with open ('projects.json') as p:
	project = json.load(p)


for name in project:
	#print name['projectId']
	command2 = "gcloud config set project " + str(name['projectId']) 
	output1 = sp.call(command2, shell=True)
	command3 = "gcloud compute networks list --format json > vpc.json 2>ERROR.txt"
	output2 = sp.call(command3, shell=True)
        if output2 == 0:
	    with open ('vpc.json') as v:
		vpc = json.load(v)
	    for vpcname in vpc:
		#print(vpcname['name'])
	        if vpcname['name'] == "default" and vpcname['description'] == "Default network for the project":
                    print ("Default VPC is enabled for " + name['name'])
                else:
                    print("Default VPS is desabled for " + name['name'])
        else:
            print("Please enable Billing and Compute API for the project " + name['name'])
