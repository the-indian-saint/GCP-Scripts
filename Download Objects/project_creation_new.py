#!/user/bin/python
import os
import sys
import subprocess as sp

#Take inputs
print("Please make sure your account has IAM & Billing permissions to create projects under an Organisation or a Folder.")
print("Click on the link https://cloud.google.com/iam/docs/overview to know more.")
project_name = raw_input("Provide a project name ")
print("Provide an Organization ID below, only if you want this project created directly under that Organization(Not inside any Folder) or press Enter to provide a Folder ID.")

# check if the org id is provided or not


try:
    organisation = raw_input("Organization ID :")
except SyntaxError, organisation:
    print("No Organization provide")
    
if len(organisation) == 0:
    print("Provide a folder ID below, if you want this project created under a folder. If Organization id is provided above, then press Enter on the keyboard")
    try:
        folder = raw_input("Folder ID: ")
    except SyntaxError, folder:
        folder = None

 
string1 = "gcloud projects create "
string3 = " --no-enable-cloud-apis" + " --folder " + folder
string889 = " --no-enable-cloud-apis" + " --organization "  + organisation
string2 = " --name " + project_name.lower()
project_id = "dm-"+project_name.lower()+"-126544"
string4 = string1  + project_id + string2 + string3
string998 = string1 + project_id + string2 + string889

#define the main function


def project_creation():
    if output == 0:
        print("Project Created " + project_id)
        billing_account = raw_input(" Provid Billing Account ID ")
        string5 = "gcloud alpha billing projects link " + project_id + " --billing-account " + billing_account
        output2 = sp.call(string5, shell=True)
        if output2 == 0:
            print("Billing Account " + billing_account + " is linked with " + project_id)
            string10 = "gcloud config set project " + project_id
            os.system(string10)
            print("Please waite. Enabling Compute API.")
            string9 = "gcloud services enable compute.googleapis.com"
            os.system(string9)
            print("Compute API enabled")
            input3 = raw_input("Type 'yes' if you want to create a bucket for " + project_name + " ")
            if input3.lower() == "yes":
                string100 = "gcloud services enable storage-component.googleapis.com storage-api.googleapis.com"
                bucket_name = raw_input("Provide a unique name for the bucket ")
                region = raw_input("provide the region name ")
                string111 = bucket_name
                string112 = "gsutil mb -l " + region + " gs://" + string111
                output10 = sp.call(string112 , shell=True)
                if output10 == 0: 
                    print("Bucket Created")
                    print("Bucket Name: " + string111)
                else:
                    print("Bucket name is not unique. Try Again...")
                    bucket_name1 = raw_input("Bucket Name: ")
                    stirng99 = "gsutil mb -l " + region + " gs://" + bucket_name1
                    output111 = sp.call(string99, shell=True)
                    if output111 == 0:
                        print("Bucket Created")
                        print("Bucket Name: " + bucket_name1)
                    else:
                        print("Bucket Creation Failed.")
                        print("Create a bucket manually afterwords.")
                        print('''Use the command "gsutil mb -l 'Region' gs://'Bucket_Name'" to create a bucket from CLI''')
            else:
                print("No bucket is created. Continue to delete the default VPC")
            input331 = raw_input("Tpye 'Yes' if you want to delete the Default VPC in " +project_name + "." + " Or press Enter to continue")
            if input331.lower() == "yes":
                #print(" First Need to delete the firewall rules assiciated with the Default VPC, press 'y' to continue")
                #print("Press 'y' if you want to delete the Default VPC in " + project_name + "or press 'n'")
                string7 = "gcloud compute firewall-rules delete default-allow-icmp default-allow-internal default-allow-rdp default-allow-ssh -q"
                os.system(string7)
                #print("Deleting the Default VPC, press 'y'")
                string8 = "gcloud compute networks delete default -q"
                os.system(string8)
            else:
                print("Project created with Default VPC enabled.")
        else:
            print("Unable to link the given project id to the Billing Account.")
            print("Make sure the Billing Account ID is correct or the number of assigned projects has not exceeded the quota for the billing account.") 
            print("Deleting the new project...")
            string55 = "gcloud projects delete " + project_id + " -q"
            os.system(string55)
            print("You will not able to create a project with the same name for next 24 hours. Please provide a different project name if you want to rerun the script within 24 hours")
            sys.exit(0)
    else:
        sys.exit()
if len(organisation) == 0:
    #print ("I am in if")
    output = sp.call(string4, shell=True)
    project_creation()
else:
    #print("I am in else")
    output = sp.call(string998, shell=True)
    project_creation()

