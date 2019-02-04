import os
import subprocess as sp
import datetime
from configparser import *


config = ConfigParser()
config.read("config.ini")
source_folder = config.get("myconfig", "source_folder")
destination_folder = config.get("myconfig", "destination_folder")
extension = config.get("myconfig", "extension")
server_name = config.get("myconfig", "server_name")
    
#commmand = '''"gcloud auth activate-service-account project-creation@brave-watch-214012.iam.gserviceaccount.com --key-file "D:\brave-watch-214012-2b70340afa90.json"'''
def localToBucket(source_folder):
    for filename in os.listdir(source_folder):
        #if filename.endswith(".rar"):
            #print(filename)
        path = source_folder + "\\" + str(filename)
        t = os.path.getmtime(path)
        readable_date = datetime.datetime.fromtimestamp(t).date().isoformat()      
        cp_file = "gsutil cp -r " + path + " " + destination_folder + "/" + server + "/" + str(readable_date) + "/"
        os.system(cp_file)
        remove_path = source_folder + "\\" + str(filename)
        #os.remove(remove_path)            
localToBucket(source_folder)
