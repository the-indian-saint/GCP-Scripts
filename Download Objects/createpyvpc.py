from googleapiclient import discovery
from oauth2client.client import GoogleCredentials



credentials = GoogleCredentials.get_application_default()
service = discovery.build('cimpute', 'v1', credentials=credentials)
project_body = {
                {
"name":"
testvpc2
"
"IPv4Range":"
10.0.0.0/16
"
"subnetworks":
[
"
10.0.0.0/24
"


]

}
            }
request = service.networks().insert(body=project_body)
request.execute()
print(request)





