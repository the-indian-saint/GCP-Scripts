#!/user/bin/python
import os

project_id = raw_input('name of the project')

string = 'gcloud config set project ' + project_id.lower()
os.system(string)

string2 = "gcloud services enable compute.googleapis.com"
os.system(string2)

string3 = "gcloud config set project rohan-project-213912"
os.system(string3)


