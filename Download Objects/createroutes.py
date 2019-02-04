import subprocess as sp
import os
from configparser import *
import daytime
import sys



config = ConfigParser()
config.read("createroute.config")


route_name = config.get("myconfig", "route_name")
#next hop type can be address, gateway, instance or vpn-tunnel
next_hop_type = config.get("myconfig", "next_hop_type") 
destination = config.get("myconfig", "destination")
network = config.get("myconfig", "network")
next_hop = config.get("myconfig", "next_hop")
priority = config.get("myconfig", "priority")


command = "gcloud compute routes create %s --destination-range %s --next-hop-%s %s --network %s --priority %s" %(route_name[1:-1], destination[1:-1], next_hop_type[1:-1], next_hop[1:-1], priority[1:-1])
os.system(command)

