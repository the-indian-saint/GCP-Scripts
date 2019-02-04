from google.cloud import storage
from google.cloud.storage import Blob
from googleapiclient import discovery
import time
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_project(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
   # print(f"Processing file: {file['name']}.")

    client = storage.Client()
    bucket = client.get_bucket('autocreatebucket')
    # Then do other things...
    blob = bucket.get_blob('accountvreationtest.xlsx')
    #print(blob.download_as_string())

    with open('/tmp/accountcreationtest.csv', 'wb') as file_obj:
        blob.download_to_file(file_obj)
    with open('/tmp/accountcreationtest.csv', 'r') as acc_file:
        reader_dict = csv.DictReader(acc_file, delimiter="\t")
        for row in reader_dict:
            Project_Id = row['Project_Id']
            Project_Name = row['Project_Name']
            Organization_Id = row['Org_Id']
            service = discovery.build('cloudresourcemanager', 'v1')
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
            print(res)
            time.sleep(60)
            service_bill = discovery.build('cloudbilling', 'v1')

            list_billing_account = service_bill.billingAccounts().list().execute()

            print(list_billing_account['billingAccounts'][0]['name'])

            bill_acc_name = list_billing_account['billingAccounts'][0]['name']

            req = {"name": 'projects/' + Project_Id + '/billingInfo', "projectId": Project_Id,
                   "billingAccountName": bill_acc_name,
                   "billingEnabled": True}
            enable_billing = service_bill.projects().updateBillingInfo(name='projects/' + Project_Id,
                                                                       body=req).execute()
            time.sleep(120)

            srv = discovery.build('compute', 'v1')
            fw_req = srv.firewalls().list(project=Project_Name)
            fw_res = fw_req.execute()
            for firewall in fw_res:
                fw_req2 = srv.firewalls().delete(project=Project_Name, firewall=firewall['name'])
                print(fw_req2)
            time.sleep(30)
            vpc_req = srv.networks().delete(project=Project_Name, network="default")
            vpc_res = vpc_req.execute()

            time.sleep(30)
            msg = MIMEMultipart()
            msg["Subject"] = "New Account Creation "
            msg["From"] = "Sindhu Reddy <sin.rdd@echonetechnologies.com>"
            msg["To"] = "rohan.matkar489@gmail.com"
            msg["Cc"] = "rohan.matkar@outlook.com"
            table_heading = "<th bgcolor='#5DADE2'>Configuration Item</th><th bgcolor='#5DADE2'>Value</th>"
            html = """\
            <p>A Project ({Project_Name}) has been created in AWS /GCP..<br/>
            </p>
            <br/><br/>
            <span>
            <p>Please provide the networking information using the following URL.<p/>
            <p>(URL) http://SERVER NAME<p/>
            <p>Once you have submitted the information with the above link, you will be provided with a �Record Number�<p/>
            <p>You may then close this INC referencing this Record Number.<p/>
            <p>Any questions please contact Hybrid Cloud Ops<p/>
            </span>""".format(Project_Name=Project_Name)
            msgHtml = MIMEText(html, 'html')
            msg.attach(msgHtml)
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("sin.rdd@echonetechnologies.com", "MOMLOVE19")
            s.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
            s.quit()







