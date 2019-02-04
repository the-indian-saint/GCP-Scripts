import os
import subprocess as sp
import json

command = "gcloud projects list --format json > projects.json"
sp.call(command,shell=True)



with open ('projects.json') as p:
	project = json.load(p)

for name in project:
	command2 = "gcloud config set project " +  str(name['projectId'])
	sp.call(command2, shell=True)
	print("External Ip address in project " + str(name['projectId']))
	command3 = 'gcloud compute addresses list'
	sp.call(command3, shell=True)
