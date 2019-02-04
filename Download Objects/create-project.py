#!/user/bin/python
import subprocess
import os
import sys

project_name = raw_input("Provide a project name ")
bucket_name = raw_input("Provide a bucket name ")
billing_account = raw_input("Billing Account ID ")
organisation = raw_input('Provide organisation ID ')
folder = raw_input("Provide a folder id ")


string1 = "gcloud projects create "
string3 = " --no-enable-cloud-apis" + " --organization "  +organisation + " --folder " + folder
string2 = " --name " + project_name.lower()
project_id = "dm-"+project_name.lower()+"-126544"
string4 = string1  + project_id + string2 + string3
os.system(string4)
print(string4)
#string5 = "gcloud alpha billing projects link " + project_id + " --billing-account " + billing_account
#os.system(string5)

#string6 = "gcloud config set project " + project_id
#os.system(string6)

#string9 = "gcloud services enable compute.googleapis.com storage-component.googleapis.com storage-api.googleapis.com"
#os.system(string9)

#string7 = "gcloud compute firewall-rules delete default-allow-icmp default-allow-internal default-allow-rdp default-allow-ssh"
#os.system(string7)

#string8 = "gcloud compute networks delete default"
#os.system(string8)



#string11 = "gsutil mb -l us-east1 gs://" + bucket_name.lower()
#os.system(string11)

#string10 = "gcloud config set project brave-watch-214012"
#os.system(string10)

print('New project created.')
print('Project ID is ' + project_id)
print('Project Name is '+ project_name.lower())
print('Default VPC is deleted')

