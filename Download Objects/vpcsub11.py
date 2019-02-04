import csv
#from googleapiclient import discovery
#from oauth2client.client import Googlecredentials
import os
import subprocess as sp
import sys

with open ('vpc.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        for values in data:
                vpc = values['vpc']
                subnet_mode = values['subnet_mode']
                routing = values['routing']
                project = values['project']
                subnet = values['subnet']
                IPrange = values['IPrange']
                region = values['region']
                pr_google_access = values['pr_google_access']
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
                if pr_google_access.lower() == 'yes':
                   createsubnet = "gcloud compute networks subnets create %s --network %s --range %s --region %s --enable-flow-logs --enable-private-ip-google-access" %(subnet, vpc, IPrange, region)
                   os.system(createsubnet)
                   #print(createsubnet)
                else:
                   createsubnet = "gcloud compute networks subnets create %s --network %s --range %s --region %s --enable-flow-logs" %(subnet, vpc, IPrange, region)
                   os.system(createsubnet)
                   #print(createsubnet)

