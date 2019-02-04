import subprocess as sp

#Take inputs
print("Please make sure your account has IAM & Billing permissions to create projects under an Organisation or a Folder.")
print("Please refer the link https://cloud.google.com/iam/docs/overview in the browser to know more.")
project_name = raw_input("Provide a project name ")
print("Provide an Organization ID below, only if you want this project created directly under that Organization(Not inside any Folder) or press Enter to provide a Folder ID.")

# check if the org id is provided or not


try:
    organisation = raw_input("Organization ID :")
except SyntaxError:
    organisation = None
print(organisation)    
print("Provide a folder ID below, if you want this project created under a folder")
folder = raw_input("Folder ID: ")

 
string1 = "gcloud projects create "
string3 = " --no-enable-cloud-apis" + " --folder " + folder
string889 = " --no-enable-cloud-apis" + " --organization "  + organisation
string2 = " --name " + project_name.lower()
project_id = "dm-"+project_name.lower()+"-126544"
string4 = string1  + project_id + string2 + string3
string998 = string1 + project_id + string2 + string889
output = sp.call(string4, shell=True)
print(output)
#print(organisation)
if organisation == None: 
    output = sp.call(string4, shell=True)
    project_creation(output)
    print(output)
    
#else:
    #output = sp.call(string998, shell=True)
    #project_creation(output)
    #print(output)
