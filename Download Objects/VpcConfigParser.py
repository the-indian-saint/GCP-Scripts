import subprocess as sp
import os
from configparser import *
import daytime
import sys



config = ConfigParser()
config.read("createVPC.config")
subnetNumber = config.get("myconfig", "number-of-subnets")
vpc = config.get("myconfig", "vpc_name")
project = config.get("myconfig", "project_id")
bucket_required =  config.get("myconfig", "bucket_required")
cloudrouter = config.get("myconfig", "cloudroutername")
cr_region = config.get("myconfig", "cloudrouter_region")
interconnect_name = config.get("myconfig", "interconnect_name")
VLAN_attachment = config.get("myconfig", "VLAN_ATTACHMENT_NAME")
ASN = config.get("myconfig", "ASN")



try:
	bucket_name = config.get("myconfig", "bucket_name")
	bucket_region = config.get("myconfig", "bucket_region")
	

except ValueError:
	pass

if bucket_required.lower() == "yes":
	
if subnetNumber > 4:
	print("Can not create more than 4 subnets at a time, fisrt 4 subnets will be taken from the file. Run the script again to add more subnets")

subnet1 = config.get("myconfig", "subnet1_name")
subnet1_region = config.get("myconfig", "subnet1_region")
subnet1_CIDR = config.get("myconfig", "subnet1_CIDR")


subnet2 = config.get("myconfig", "subnet2_name")
subnet2_region = config.get("myconfig", "subnet2_region")
subnet2_CIDR = config.get("myconfig", "subnet2_CIDR")

subnet3 = config.get("myconfig", "subnet3_name")
subnet3_region = config.get("myconfig", "subnet3_region")
subnet3_CIDR = config.get("myconfig", "subnet3_CIDR")

subnet4 = config.get("myconfig", "subnet4_name")
subnet4_region = config.get("myconfig", "subnet4_region")
subnet4_CIDR = config.get("myconfig", "subnet4_CIDR")


project_command = "gcloud config set project %s" %(project[1:-1])
os.system(project_command) 
vpc_command = "gcloud compute networks create %s --bgp-routing-mode global --subnet-mode custom" %(vpc[1:-1])
os.system(vpc_command)

subnet1_command = "gcloud compute networks subnets create %s --network %s --range %s --enable-flow-logs --region %s") %(vpc[1:-1], subnet1[1:-1], subnet1_CIDR[1:-1], subnet1_region[1:-1])    
subnet2_command = "gcloud compute networks subnets create %s --network %s --range %s --enable-flow-logs --region %s") %(vpc[1:-1], subnet2[1:-1], subnet2_CIDR[1:-1], subnet2_region[1:-1])
subnet3_command = "gcloud compute networks subnets create %s --network %s --range %s --enable-flow-logs --region %s") %(vpc[1:-1], subnet3[1:-1], subnet3_CIDR[1:-1], subnet3_region[1:-1])
subnet4_command = "gcloud compute networks subnets create %s --network %s --range %s --enable-flow-logs --region %s") %(vpc[1:-1], subnet4[1:-1], subnet4_CIDR[1:-1], subnet4_region[1:-1])

os.system(subnet1_command)
os.system(subnet2_command)
os.system(subnet3_command)
os.system(subnet4_command) 


try:
	bucket command ="gsutil mc -c regional -l %s gs://%s" %(bucket_region[1:-1], bucket_name[1:-1])

except ValueError:
	pass

crcommand = "gcloud compute routers create %s --network %s --asn %s --advertisement-mode default --region %s" %(cloudrouter[1:-1], vpc[1:-1], ASN[1:-1], cr_region[1:-1])
os.system(crcommand)

intername = "projects/%s/global/interconnects?%s" %(project[1:-1], interconnect_name[1:-1])

vlancommand = "gcloud compute inteconnects attachments dedicated create %s --interconnect %s --router %s" %(VLAN_attachment[1:-1], intername, cloudroutername[1:-1])
os.system(vlancommand)

