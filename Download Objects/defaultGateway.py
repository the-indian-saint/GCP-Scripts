import subprocess as sp
import os
import sys
import csv



VPC = raw_input("Name for the VPC ")
command1 = "gcloud compute networks create " + VPC + " --bgp-routing-mode global --subnet-mode custom"
#sp.call(command1, shell=True)
command3 = "gcloud compute routes list > routes.csv"
sp.call(command3, shell=True)

with open ('routes.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader: 
            print row[3]

subnetNum = raw_input("Provide the Number of Subnets required ")

for sub in range (1, int(subnetNum)):
    Subnet = raw_input("Provide name for Subnet" + str(sub))
    CIDR = raw_input("Provide CIDR for " + Subnet)
    region = raw_input("Provide region for " + Subnet)
    command2 = "gcloud compute networks subnets create " + Subnet + " --network " + VPC + " --range " + CIDR + " --enable-flow-logs" + " --region " + region
    #sp.call(command2, shell=True)
                                                    


