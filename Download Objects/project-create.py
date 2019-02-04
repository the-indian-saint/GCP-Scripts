#!/user/bin/python
import os

project_id = raw_input("Provide a project name ")
#bucket_name = raw_input("Provide a bucket name ")
string1 = "gcloud projects create "
string3 = " --no-enable-cloud-apis"
string2 = project_id.lower()
string4 = string1 + string2 + string3
#os.system(string4)  
print(string4)
