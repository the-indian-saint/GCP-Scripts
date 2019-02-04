import csv
import os
import subprocess as sp
import json





with open ('listoutput.json', 'r') as routes_file:
    data = json.load(routes_file)
    for values in data:
        print(values)
        name = values['name']
        network = values['network']
        #dest_range = values['DEST_RANGE']
        #next_hop = values['NEXT_HOP']

        print(name)
        print(network)
        #print(dest_range)
        #print(next_hop)
