import os
import subprocess as sp
import json
import csv


project_comm = "gcloud projects list --format json > buck_prj.json"
sp.call(project_comm, shell=True)

with open ('buck_prj.json') as p:
	project = json.load(p)
for name in project:
	set = "gcloud config set project " + str(name['projectId'])
	sp.call(set, shell=True)
        command1 = "gsutil ls > bucket.json"
        sp.call(command1, shell=True)
        with open  ('bucket.json') as b:
            bucket = csv.reader(b, delimiter=' ')
            for bucketname in bucket:
                new_buck = str(bucketname)[2:-2]
                #print(str(new_buck))
                command2 = "gsutil acl get " + str(new_buck) + " > acl.json"
                sp.call(command2, shell=True)
                with open ('acl.json') as a:
                    acl = json.load(a)
                    for rules in acl:
                        #print(rules['entity'])
                        if rules['entity'] == "allUsers":
                            print(str(new_buck) + " has Public access.")
