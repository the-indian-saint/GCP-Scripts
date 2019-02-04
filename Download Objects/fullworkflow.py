from google.cloud import storage
from google.cloud.storage import Blob
from googleapiclient import discovery
import time
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

client = storage.Client()
bucket = client.get_bucket('autocreatebucket')
blob = bucket.get_blob('accountcreationtest.csv')
with open ('autocreationtest.csv', 'w') as csv_file:
	blob.download_to_file(csv_file)
with open ('autocreationtest.csv', 'r') as dow_file:
	reader = csv.DictReader(dow_file, delimiter=",")
	for row in reader:
	    Project_Id = row['Project_Id']
        Project_Name = row['Project_Name']
        Organization_Id = row['Org_Id']
	    Billing_Account = row['Billing_Account']
        service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
        project_body = {
            'name': Project_Name,
            'projectId': Project_Id,
            'parent': {
                'type': 'organization',
                'id': Organization_Id
            }
        }
        request = service.projects().create(body=project_body)
        res = request.execute()
        time.sleep(60)
	    service_bill = discovery.build('cloudbilling', 'v1', credentials=credentials)
        list_billing_account = service_bill.billingAccounts().list().execute()
        bill_acc_name = list_billing_account['billingAccounts'][0]['name']
	    bill_body = {"name": 'projects/' + Project_Id + '/billingInfo', "projectId": Project_Id,"billingAccountName": bill_acc_name,"billingEnabled": True}
	    enable_billing = service_bill.projects().updateBillingInfo(name='projects/' + Project_Id, body=bill_body).execute()
	    time.sleep(300)
	    compute = discovery.build('compute', 'v1', credentials=credentials)
	    fw_req = compute.firewalls().list(project=Project_Id)
	    fw_res = fw_req.execute()
	    for firewall in fw_res:
	        fw_req2 = compute.firewalls().delete(project=Project_Name, firewall = firewall['name'])
	        fw_res2 = fw_req2.execute()
	    time.sleep(120)
	    vpc_req = compute.networks().delete(project=Project_Name, network="default")
	    vpc_res = vpc_req.execute()
	    msg = MIMEMultipart()
            msg["Subject"] = "New Account Creation "
            msg["From"] = "from email id"
            msg["To"] = "to email id"
            msg["Cc"] = "cc email id"
            table_heading = "<th bgcolor='#5DADE2'>Configuration Item</th><th bgcolor='#5DADE2'>Value</th>"
	    html = """\
            <p>A Project ({Project_Name}) has been created in GCP..<br/>
            </p>
            <br/><br/>
            <span>
	    <p>Attached Billing account is {Billing_Account}
            <p>Please provide the networking information using the following URL.<p/>
            <p>(URL) http://SERVER NAME<p/>
	    <p>Once you have submitted the information with the above link, you will be provided with a 'Record Number'.<p/>
            <p>You may then close this INC referencing this Record Number.<p/>
            <p>Any questions please contact Hybrid Cloud Ops<p/>
            </span>""".format(Project_Name=Project_Name, Billing_Account=Billing_Account)
            msgHtml = MIMEText(html, 'html')
            msg.attach(msgHtml)
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("sin.rdd@echonetechnologies.com", "MOMLOVE19")
            s.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
            s.quit()
