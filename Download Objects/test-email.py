#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import subprocess as sp
import time
import csv


def send_email():
    msg = MIMEMultipart()
    msg['Subject'] = 'New Project Creation'
    msg['From'] = 'sindhu.thudi@citi.com'
    msg['To'] = 'sindhu.thudi@citi.com'
    msg['Cc'] = 'sai.vamsi.bharadwajkakunuri@citi.com'
    table_heading = \
        "<th bgcolor='#5DADE2'>Configuration Item</th><th bgcolor='#5DADE2'>Value</th>"
    html = \
        """\
         <p>Project({projectId}) has been created in GCP..<br/>
         </p>
         <br/><br/>
        <span>
        <p>Foundational Services have been successfully Implemented for the new project. SNOW Request has been initiated for Network team to request the VPC Creation information.<p/>
        <p>Any questions please contact Hybrid Cloud Ops<p/>
        </span>""".format(projectId=projectId,
            customeRole=roleName)
    msgHtml = MIMEText(html, 'html')
    msg.attach(msgHtml)
    s = smtplib.SMTP(host='imbapprelay.wlb2.nam.nsroot.net', port=25)
    s.sendmail(msg['From'], msg['To'].split(',') + msg['Cc'].split(','
               ), msg.as_string())
    s.quit()


def send_email_failed():
    msg = MIMEMultipart()
    msg['Subject'] = 'Role Creation Failed'
    msg['From'] = 'sindhu.thudi@citi.com'
    msg['To'] = 'sindhu.thudi@citi.com'
    msg['Cc'] = 'sai.vamsi.bharadwajkakunuri@citi.com'
    table_heading = \
        "<th bgcolor='#5DADE2'>Configuration Item</th><th bgcolor='#5DADE2'>Value</th>"
    html = \
        """\
         <p>Project({projectId}) has been created in GCP..<br/>
         </p>
         <br/><br/>
        <span>
        <p>Failed to setup the Foundational Services  Please investigate the logs for details.<p/>
        </span>""".format(projectId=projectId)
    msgHtml = MIMEText(html, 'html')
    msg.attach(msgHtml)
    s = smtplib.SMTP(host='imbapprelay.wlb2.nam.nsroot.net', port=25)
    s.sendmail(msg['From'], msg['To'].split(',') + msg['Cc'].split(','
               ), msg.as_string())
    s.quit()


def send_email_2():
    msg = MIMEMultipart()
    msg['Subject'] = \
        'Networking Information Required for new Project Setup.'
    msg['From'] = 'sindhu.thudi@citi.com'
    msg['To'] = 'sindhu.thudi@citi.com'
    msg['Cc'] = 'sai.vamsi.bharadwajkakunuri@citi.com'
    table_heading = \
        "<th bgcolor='#5DADE2'>Configuration Item</th><th bgcolor='#5DADE2'>Value</th>"
    html = \
        """\
         <p>Project({projectId}) has been created in GCP..<br/>
         </p>
         <br/><br/>
        <span>
        <p>A Service Now request has been raised for your group to provide the information to create VPC. Please follow the following steps:<p/>
        <p>1. Click on the following link http://server and submit the information. You will be provided a Reference number after you submit the form.<p/>
		<p>2. Go to Service Now and update the Service now ticket with the following Information.<p/>
		<p>Once VPC is created , you will be contacted by HYBRID CLOUD OPS team.<p/>
        </span>""".format(projectId=projectId)
    msgHtml = MIMEText(html, 'html')
    msg.attach(msgHtml)
    s = smtplib.SMTP(host='imbapprelay.wlb2.nam.nsroot.net', port=25)
    s.sendmail(msg['From'], msg['To'].split(',') + msg['Cc'].split(','
               ), msg.as_string())
    s.quit()


# roleName = raw_input("Provide a name for the role")
# projectId = raw_input("Provide a project ID")

with open('csvfile.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    for values in data:

        # print(values)

        #print values['RoleName']
        #print values['ProjectID']
        roleName = values['RoleName']
        projectId = values['ProjectID']
        command = \
            'gcloud iam roles create %s --project %s --file my-role-definition.yaml -q' \
            % (roleName, projectId)
        output = sp.call(command, shell=True)
        if output == 0:
            send_email()
            send_email_2()
            print ('Email Notification Sent')
        else:
            send_email_failed()
            print ('Role Creation Failed')

