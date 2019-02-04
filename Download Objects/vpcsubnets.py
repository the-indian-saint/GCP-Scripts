import csv
#from googleapiclient import discovery
#from oauth2client.client import Googlecredentials
import os
import subprocess as sp
import sys
import json
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    msg = MIMEMultipart()
    msg['Subject'] = 'VPC CREATION	'
    msg['From'] = 'sindhu.thudi@citi.com'
    msg['To'] = 'sindhu.thudi@citi.com'
    msg['Cc'] = 'sai.vamsi.bharadwajkakunuri@citi.com'
    table_heading = \
        "<th bgcolor='#5DADE2'>Configuration Item</th><th bgcolor='#5DADE2'>Value</th>"
    html = \
        """\
         <p>VPC - {vpc} has been successfully Created.. Please execute the next required steps.<br/>
         </p>
         <br/><br/>
        <span>
        </span>""".format(vpc=vpc)
    msgHtml = MIMEText(html, 'html')
    msg.attach(msgHtml)
    s = smtplib.SMTP(host='imbapprelay.wlb2.nam.nsroot.net', port=25)
    s.sendmail(msg['From'], msg['To'].split(',') + msg['Cc'].split(','
               ), msg.as_string())
    s.quit()

with open ('vpc.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        for values in data:
                vpc = values['vpc']
                subnet_mode = values['subnet_mode']
                routing = values['routing']
                project = values['project']
                subnet = values['subnet']
                IPrange = values['IPrange']
                region = values['region']
                pr_google_access = values['pr_google_access']
                changeprj = "gcloud config set project %s &> /dev/null" %(project)
                os.system(changeprj)
                if subnet_mode.lower() == 'auto':
                        createvpc = "gcloud compute networks create %s --bgp-routing-mode %s --subnet-mode auto" %(vpc, routing)
                        # output = sp.call(createvpc, shell=True)
                        output=sp.call(createvpc, shell=True)
                        if output == 0:
                            send_email()
                        #print(createvpc)
                else:

                        #print("INSIDE SUBNET MODE ELSE ")
                        createvpc = "gcloud compute networks create %s --bgp-routing-mode %s --subnet-mode %s" %(vpc, routing, subnet_mode)
                        # output = sp.call(createvpc, shell=True)
                        os.system(createvpc)
                        #print(createvpc)
                        #print(output)

                #if output == 0:
                if pr_google_access.lower() == 'yes':
                        #print("INSIDE YES ")
                        createsubnet = "gcloud comllllpute networks subnets create %s --network %s --range %s --region %s --enable-flow-logs --enable-private-ip-google-access" %(subnet, vpc, IPrange, region)
                        os.system(createsubnet)
                        #print(createsubnet)
                        route_command = "gcloud compute routes list --format json > routes.json"
                        os.system(route_command)
                        with open ('routes.json', 'r') as routes:
                            data = json.load(routes)
                            for values in data:
                                name = values['name']
                                network = values['network']
                                dest_range = values['destRange']
                                vpc_self = "https://www.googleapis.com/compute/v1/projects/%s/%s/networks/%s" %(project, routing, vpc)
                                if network == vpc_self:
                                    if str(dest_range) == "0.0.0.0/0":
                                        del_command = "gcloud compute routes delete %s -q" %(name)
                                        output2=sp.call(del_command, shell=True)
                                        if output2 == 0:
                                            send_email()

                else:

                        #print("INSIDE ELSE ")
                        createsubnet = "gcloud compute networks subnets create %s --network %s --range %s --region %s --enable-flow-logs" %(subnet, vpc, IPrange, region)
                        os.system(createsubnet)
                        #print(createsubnet)
                        route_command = "gcloud compute routes list --format json > routes.json"
                        os.system(route_command)
                        with open ('routes.json', 'r') as routes:
                            data = json.load(routes)
                            for values in data:
                                name = values['name']
                                network = values['network']
                                dest_range = values['destRange']
                                vpc_self = "https://www.googleapis.com/compute/v1/projects/%s/%s/networks/%s" %(project, routing, vpc)
                                if network == vpc_self:
                                    if str(dest_range) == "0.0.0.0/0":
                                        del_command = "gcloud compute routes delete %s -q" %(name)
                                        output2 = sp.call(del_command, shell=True)
                                        if output == 0:
                                            send_email()




time.sleep(60)
print("Creating Firewall rule")


command2 = "python create_firewall_rule.py"
os.system(command2)





