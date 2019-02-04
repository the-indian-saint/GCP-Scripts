import subprocess as sp
import os
from configparser import *
import datetime
import sys



config = ConfigParser()
config.read("createVPC.config")
subnetNumber = config.get("myconfig", "number-of-subnets")
crNumber = config.get("myconfig", "number-of-cloudRouters")
ASN = config.get("myconfig", "ASN")






def createVPC():
	VPC = raw_input("Name for the VPC ")
	command = "gcloud compute networks create " + VPC + " --bgp-routing-mode global --subnet-mode custom"
	output1 = sp.call(command, shell=True)
	return VPC


	
def createSubnet():
	subNet = raw_input("Name for Subnet" + str(x) + ": ")
	CIDR = raw_input("CIDR for the subnet " + subNet + ": ")
	region = raw_input("Region for the subnet " + subNet + ": ")
	command = "gcloud compute networks subnets create " + subNet + " --network " + vpcName + " --range " + CIDR + " --enable-flow-logs" + " --region " + region 
	output2 = sp.call(command, shell=True)
        return subNet
        
        
        #if output2 != 0:
            #command2 = "gcloud compute networks delete " + VPC
            #os.system(command2)
            #sys.exit()

	
	
def createCloudRouter():
    CloudRouter = raw_input("Name for Cloud Router" + str(y) + ": ")
    CrRegion = raw_input("Region for " + CloudRouter + ": ")
    command = "gcloud compute routers create " + CloudRouter + " --network " + vpcName + " --asn " + ASN[1:-1] + " --advertisement-mode default" + " --region " + CrRegion
    output = sp.call(command, shell=True)
    #print(command)
    return CloudRouter
    #if output != 0:


def createVLAN():
	projectID = raw_input("Provide the Project ID of the Interconnect: ")
	InterName = raw_input("Provide a name for the Interconnect: ")
        attachName = raw_input("Provide a name for the VLAN attachment: ")
	intername = "projects/" + projectID + "/global/interconnects/" + InterName
	command = "gcloud compute interconnects attachments dedicated create " + attachName + " --interconnect " + intername + " --router " + Crouter
	output = sp.call(command, shell=True)
        #print(command)
	return attachName

def configCrouter():
	peername = raw_input("Provide a peer name to configure the Cloud Router: ")
	peerasn = raw_input("Provide peer ASN: ")
	command = "gcloud compute routers update-bgp-peer --name " + Crouter + " --peer-name " + peername + " --peer-asn " + peerasn
	output = sp.call(command, shell=True)
        #print(command)



vpcName = createVPC()
subnetlist = {}
routerlist = {}
	
for x in range (1, 100):
    name = "Subnet" + str(x)
    Subnet = createSubnet()
    print(name + " = " + Subnet)
    subnetlist[name] = Subnet
    if x == int(subnetNumber[1:-1]):
        break

for y in range (1,100):
    name = "Cloud Router" + str(y)
    Crouter = createCloudRouter()
    print(name + " = " + Crouter)
    routerlist[name] = Crouter
    for z in range (1,100):
        vlan = "Interconnect" + str(z)
        vlanattach = createVLAN()
        configCrouter()
        onprem = "gcloud compute interconnects attachments describe " + vlanattach
        sp.call(onprem, shell=True)
        #print(onprem)
        if z == int(crNumber[1:-1]):
                break
    if y == int(crNumber[1:-1]):
        break


