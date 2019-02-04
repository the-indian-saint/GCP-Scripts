import urllib3.request
import json

project = raw_input("Provide Project ID: ")

key = '9197bfea32126d240fe9b34c31bcf0700b450b9e'
data = 'https://www.googleapis.com/compute/v1/projects/%s/aggregated/instances %s(project)'
full_url = data + key
response = urllib3.request.urlopen(full_url)


for instance in response:
    print(instance)
