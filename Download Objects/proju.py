#!/user/bin/python
import os
import sys
import subprocess as sp

#generate logs in project_creation.logs
os.system("echo ---------------------------------------------- >> project_creation.logs")
os.system("date >> project_creation.logs")
os.system(" gcloud auth list >> project_creation.logs")


#Take inputs
print("Please make sure your account has IAM & Billing permissions to create projects under an Organisation or a Folder.")
print("Click on the link https://cloud.google.com/iam/docs/overview to know more.")

project_name = 'fbdghty67890'
project_name_string = " echo Name of the provided project: " + project_name + "  >> project_creation.logs"
os.system(project_name_string)

organisation = ''
provided_org = "echo Org ID: " + organisation + "  >> project_creation.logs"
os.system(provided_org)

folder = '399719623950'
provided_folder = " echo Folder ID: " + folder + " >> project_creation.logs"
os.system(provided_folder)


string1 = "gcloud projects create "
try:
    string3 = " --no-enable-cloud-apis" + " --folder " + folder
except NameError:
    #print("Creating project under  organization")
    pass
string889 = " --no-enable-cloud-apis" + " --organization "  + organisation
string2 = " --name " + project_name.lower()
project_id = "dm-"+project_name.lower()+"-126544"
try:
    string4 = string1  + project_id + string2 + string3
except NameError:
    #print("Starting Project creation....")
    pass
string998 = string1 + project_id + string2 + string889





def project_creation():
    if output == 0:
        print("Project Created " + project_id)
        os.system("echo Project Creation sussessful >> project_creation.logs")
        billing_account = '013776-D7FA9A-505E56'
        string5 = "gcloud alpha billing projects link " + project_id + " --billing-account " + billing_account
        output2 = sp.call(string5, shell=True)
        if output2 == 0:
            print("Billing Account " + billing_account + " is linked with " + project_id)
            bill_acc = "echo Billing Account " + billing_account + " linked with " + project_id + " >> project_creation.logs"
            os.system(bill_acc)
            string10 = "gcloud config set project " + project_id + " >> project_creation.logs"
            os.system(string10)
            print("Please waite. Enabling Compute API.")
            string9 = "gcloud services enable compute.googleapis.com"
            os.system(string9)
            os.system("echo Compute API enabled >> project_creation.logs")
            print("Compute API enabled")
            input3 = 'yes'
            if input3.lower() == "yes":
                string100 = "gcloud services enable storage-component.googleapis.com storage-api.googleapis.com"
                os.system("echo Storage APIs enabled to create bucket >> project_creation.logs")
                bucket_name = 'fbad345678890'
                region = 'us-central1'
                string111 = bucket_name
                string112 = "gsutil mb -l " + region + " gs://" + string111
                output10 = sp.call(string112 , shell=True)
                if output10 == 0:
                    print("Bucket Created")
                    print("Bucket Name: " + string111)
                    os.system("echo Bucket Created >> project_creation.logs")
                else:
                    print("Bucket name is not unique. Try Again...")
                    bucket_name1 = 'project_name'
                    string99 = "gsutil mb -l " + region + " gs://" + bucket_name1
                    output111 = sp.call(string99, shell=True)
                    if output111 == 0:
                        print("Bucket Created")
                        print("Bucket Name: " + bucket_name1)
                        os.system("echo Bucket Created >> project_creation.logs")
                    else:
                        print("Bucket Creation Failed.")
                        os.system("echo Bucket Creation Failed >> project_creation.logs")
                        print("Create a bucket manually afterwords.")
                        print('''Use the command "gsutil mb -l 'Region' gs://'Bucket_Name'" to create a bucket from CLI''')
            else:
                print("No bucket is created. Continue to disable the default VPC")
            input331 = 'yes'
            if input331.lower() == "yes":
                #print(" First Need to delete the firewall rules assiciated with the Default VPC, press 'y' to continue")
                #print("Press 'y' if you want to delete the Default VPC in " + project_name + "or press 'n'")
                string7 = "gcloud compute firewall-rules delete default-allow-icmp default-allow-internal default-allow-rdp default-allow-ssh -q"
                os.system(string7)
                #print("Deleting the Default VPC, press 'y'")
                string8 = "gcloud compute networks delete default -q"
                os.system(string8)
                os.system("echo Default VPC is disabled >> project_creation.logs")
            else:
                print("Project created with Default VPC enabled.")
                os.system("echo Default VPC is enabled >> project_creation.logs")
        else:
            print("Unable to link the given project id to the Billing Account.")
            print("Make sure the Billing Account ID is correct or the number of assigned projects has not exceeded the quota for the billing account.")
            print("Deleting the new project...")
            string55 = "gcloud projects delete " + project_id + " -q"
            os.system(string55)
            os.system("echo Failed to link the billing account.Project is deleted >> project_creation.logs")
            print("You will not able to create a project with the same name for next 24 hours. Please provide a different project name if you want to rerun the script within 24 hours")
            sys.exit(0)
    else:
        os.system("echo Project creation failed >> project_creation.logs")
        sys.exit()
if len(organisation) == 0:
    #print ("I am in folder")
    output = sp.call(string4, shell=True)
    project_creation()
else:
    #print("I am in org")
    output = sp.call(string998, shell=True)
    project_creation()


