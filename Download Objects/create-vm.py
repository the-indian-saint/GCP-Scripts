#!/user/bin/python

import os

vm_name = raw_input('Give a VM Name ')


string = "gcloud compute instances create " + vm_name + " --subnet test-subnet --zone asia-east1-a --image-family centos-6 --image-project centos-cloud --create-disk size=100GB,type=pd-standard"
os.system(string)

