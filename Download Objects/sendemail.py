import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import os
import subprocess as sp
import time
#import csv

def send_email():
        msg = MIMEMultipart()
        msg["Subject"] ="New Account Creation "
        msg["From"] = "From Email"
        msg["To"] = "to email"
        msg["Cc"] = "cc email"
        table_heading = "<th bgcolor='#5DADE2'>Configuration Item</th><th bgcolor='#5DADE2'>Value</th>"
        html = """\
         <p>Project({projectId}) has been created in GCP..<br/>
         </p>
         <br/><br/>
        <span>
        <p>Foundational Services have been Deployed({customeRole}).<p/>
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
        send_email()

