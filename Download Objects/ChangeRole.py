import os
import json
import sys
import subprocess as sp

resource_group = raw_input("Press 'o' to provide access on Organization level or press 'p' to provide access on Project level ")
#resource = raw_input("Provide a resource ")
username = raw_input("Provide an Email Id ")
role = raw_input("Provide the role ")
userinput = raw_input("Type 'a' to attach the role or type 'r' to remove the role ")




if userinput == "a":
    command = "add-iam-policy-binding"
elif userinput == "r":
    command = "remove-iam-policy-binding"
else:
    print("Wrong Input for attaching or detaching a role")
    sys.exit()

if resource_group == "o":
    group = "organizations"
    org_id = raw_input("Provide Org Id ")
    policy_comm = "gcloud " + group + " " + command + " " + org_id
elif resource_group == "p":
    group = "projects"
    prj_id = raw_input("Provide Prj ID ")
    policy_comm = "gcloud " + group + " " + command + " " + prj_id
else:
    print("Wrong Input for resource group, please press 'o' or 'p' ")
    sys.exit()

policy_command = policy_comm + " " + " --member user:" + username + " --role roles/" + role


#print (policy_command)
os.system(policy_command)


