from pprint import pprint
from oauth2client.client import GoogleCredentials
from google.cloud import storage
from google.oauth2 import service_account
import os 

credentials = service_account.Credentials.from_service_account_file(
    'C:\GIT Local Repo\Keys\crucial-inn-228012-be47e54fcf62.json')    
client = storage.Client(credentials=credentials)
bucket = client.get_bucket('pyscript')

blobs = bucket.list_blobs()

for blob in blobs:
    obj = bucket.blob(str(blob.name))
    try:
        obj.download_to_filename(str(blob.name))
    except Exception as e:
        print(e)
    if blob.name in os.listdir('.'):
        pass
    else:
        try:
            nested_name = str(blob.name).split('/')
            obj.download_to_filename(str(nested_name[-1]))
        except Exception as e:
            print(e)