import os
import csv
import os



def multi_usr():
	with open ('changeRole.csv', 'r') as csv_file:
		roles = csv.reader(csv_file)
		for users in roles:
                        
                        data = users[0].split('\t')
                        userid = data[0]
                        roles = data[1]
                        #print(data[2])
                        #print(data[3])
                        if len(data[2]) > 0:
                            #print("I am in Prj")
                            command = "gcloud projects add-iam-policy-binding " + str(data[2]) + " --member user:" + userid + " --roles roles/" + roles
                            os.system(command)

                        elif len(data[3]) > 0:
                            #print("I am in Org")
                            command = "gcloud organizations add-iam-policy-binding " + str(data[3]) + " --member user:" + userid + " --roles roles/" + roles
                            os.system(command)

                        else:
                            print("No Org or Prj provided")
multi_usr()
