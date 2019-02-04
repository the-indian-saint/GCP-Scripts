import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import subprocess as sp
import time
import csv

def send_email():
        msg = MIMEMultipart()
        msg["Subject"] ="New Account Creation "
        msg["From"] = "Sindhu Reddy <sin.rdd@echonetechnologies.com>"
        msg["To"] = "krishna.reddy0852@gmail.com"
        msg["Cc"] = "sindhuthudi@gmail.com"
        table_heading = "<th bgcolor='#5DADE2'>Configuration Item</th><th bgcolor='#5DADE2'>Value</th>"
        html = """\
         <p><b>An Account / Project({projectId}) has been created in AWS /GCP..<br/>
         </b></p>
         <br/><br/>
        <span>
        <p>A custome role has been created ({customeRole}).<p/>
        <p>Please provide the networking information using the following URL.<p/>
        <p>(URL) http://SERVER NAME<p/>
        <p>Once you have submitted the information with the above link, you will be provided with a Record Number<p/>
        <p>You may then close this INC referencing this Record Number.<p/>
        <p>Any questions please contact Hybrid Cloud Ops<p/>
        </span>""".format(projectId=projectId, customeRole=roleName)
        msgHtml = MIMEText(html, 'html')
        msg.attach(msgHtml)
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("sin.rdd@echonetechnologies.com", "MOMLOVE19")
        s.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
        s.quit()


#roleName = raw_input("Provide a name for the role")
#projectId = raw_input("Provide a project ID")

with open ('csvfile.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    for values in data:
        #print(values)
        #print(values['RoleName'])
        #print(values['ProjectID'])
        roleName = values['RoleName']
        projectId = values['ProjectID']
        command = "gcloud iam roles create %s --project %s --file my-role-definition.yaml -q" %(roleName, projectId)
        output = sp.call(command, shell=True)
        if output == 0:
            send_email()
            print("Email Notification Sent")
        else:
            print("Role Creation Failed")
 


time.sleep(5)
