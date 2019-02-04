import subprocess as sp
import os
#from configparser import *
#import daytime
import sys
import csv

with open ('firewallRules.csv','r') as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    for values in data:
        firewall_rule_name = values['Firewall_rule_name']
        action = values['firewall_action']
        port = values['firewall_port']
        fw_proto = values['firewall_protocol']
        network = values['network']


fw_command = "gcloud compute firewall-rules create %s --%s %s:%s --network %s" %(firewall_rule_name, action, fw_proto, port, network) 
os.system(fw_command)
