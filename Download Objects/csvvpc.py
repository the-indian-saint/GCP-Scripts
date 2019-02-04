import csv
#from googleapiclient import discovery
#from oauth2client.client import Googlecredentials
import os
import subprocess as sp
import sys
 



with open ('createvpc1.csv', 'r') as csv_file:
	data = csv.reader(csv_file)
	for values in data:
		vpcs = values[0].split('\t')
		vpc = vpcs[0]
		subnet_mode = vpcs[2]
		routing = vpcs[3]
		project = vpcs[1]
		subnet = vpcs[4]
		range = vpcs[5]
		region = vpcs[6]
		pr_google_access = vpcs[7]
		changeprj = "gcloud config set project %s &> /dev/null" %(project)
		os.system(changeprj)
		if subnet_mode.lower() == 'auto':
			createvpc = "gcloud compute networks create %s --bgp-routing-mode %s --subnet-mode auto 2> /dev/null" %(vpc, routing)
			output = sp.call(createvpc, shell=True)
			#print(createvpc)
		else:
			createvpc = "gcloud compute networks create %s --bgp-routing-mode %s --subnet-mode %s 2> /dev/null" %(vpc, routing, subnet_mode)
			output = sp.call(createvpc, shell=True)
			#print(createvpc)
		if output != 0:
			if pr_google_access.lower() == 'yes': 
				createsubnet = "gcloud compute networks subnets create %s --network %s --range %s --region %s --enable-flow-logs --enable-private-ip-google-access" %(subnet, vpc, range, region)
				os.system(createsubnet)
				#print(createsubnet)
			else:
				createsubnet = "gcloud compute networks subnets create %s --network %s --range %s --region %s --enable-flow-logs" %(subnet, vpc, range, region)
				os.system(createsubnet)
				#print(createsubnet)
