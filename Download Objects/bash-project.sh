#!/bin/bash
set -e
read -p "project_name= " project_name
echo "${project_name,,}" > /home/sin_rdd/project-creation-scripts/data1.txt
if [ -z "$project_name" ]
then
      exit 1
else
      echo "$project_name"
fi
read -p "bucket_name= " bucket_name
echo "$bucket_name"
if [ -z "$bucket_name" ]
then
      exit 1
else
      echo "$bucket_name"
fi
read -p 'billing_account= ' Billing_ID
echo "$Billing_ID"
if [ -z "$Billing_ID" ]
then
      exit 1
else
      echo "$Billing_ID"
fi
read -p 'organisation= ' Organisation_ID
echo "$Organisation_ID"
#if [ -z "$Organisation_ID" ]
#then
#      exit 1
#else
#      echo "$Organisation_ID"
#fi
read -p 'folder= ' Folder_Name
echo "$Folder_Name"
if [ -z "$Folder_Name" ]
then
      exit 1
else
      echo "$Folder_Name"
fi
project_id="dm-`cat /home/sin_rdd/project-creation-scripts/data1.txt`-126544"
echo "$project_id"
gcloud projects create "$project_id" --no-enable-cloud-apis --folder "$Folder_Name"  --name `cat /home/sin_rdd/project-creation-scripts/data1.txt` --organization "$Organisation_ID" 
gcloud alpha billing projects link "$project_id" --billing-account "$Billing_ID"
gcloud config set project "$project_id"
gcloud services enable compute.googleapis.com storage-component.googleapis.com storage-api.googleapis.com
gcloud compute firewall-rules delete default-allow-icmp default-allow-internal default-allow-rdp default-allow-ssh
gcloud compute networks delete default
gsutil mb -l us-east1 gs://`cat /home/sin_rdd/project-creation-scripts/data1.txt`
gcloud config set project brave-watch-214012
echo "New project created."
echo "Project ID is:   $project_id"
echo "Project Name is:    `cat /home/sin_rdd/project-creation-scripts/data1.txt"
echo "Default VPC is deleted."
rm -rf /home/sin_rdd/project-creation-scripts/data1.txt
