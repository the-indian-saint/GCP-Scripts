from re import sub
from decimal import Decimal
import csv
from billing_workflow import *

# Config Values
output_file = '2018_September_AWS_billing.csv'
shared_invoice_number = '153589787'
invoice_date = ''
invoice_billing_period = ''

# Open report file
report = open(output_file,'w')
# Write header row
report.write("invoice number|aws account" + "," + "aws account" + "," + "app id" + "," + "billing profile id" + "," + "ALLOCATION %" + "," + "GOC" + "," + "amount USD" + "," + "invoice number" + "," + "AWS_Account_Description" + "\n")

# Open input files and create data lists
with open('aws_raw_data.txt', 'rb') as awscsvfile:
    awsData = list(csv.reader(awscsvfile))

with open('goc_data.csv', 'rb') as goccsvfile:
    gocData = list(csv.reader(goccsvfile))

# Capture shared invoice value
sharedInvoiceValue = Decimal(0)
for row in awsData:
    if row[0] == shared_invoice_number:
        invoice = row[3]
        sharedInvoiceValue = sharedInvoiceValue + Decimal(sub(r'[^\d.]', '', invoice))
print "SHARED INVOICE VALUE: " + str(sharedInvoiceValue)

# Calculate total shared amount value
sharedAmountValue = Decimal(0)
for row in awsData:
    if row[0] != shared_invoice_number:
        if row[4] == 'y':
            invoice = row[3]
            sharedAmountValue = sharedAmountValue + Decimal(sub(r'[^\d.]', '', invoice))
print "SHARED VALUE IN NON SHARED INVOICE: " + str(sharedAmountValue)

# Calculate total non-shared amount value
nonSharedAmountValue = Decimal(0)
for row in awsData:
    if row[4] == 'n':
        invoice = row[3]
        nonSharedAmountValue = nonSharedAmountValue + Decimal(sub(r'[^\d.]', '', invoice))
print "NON-SHARED INVOICE VALUE: " + str(nonSharedAmountValue)

# Calculate percentage and final amount for each AWS account excluding shared accounts
auditSharedAllocationAmount = Decimal(0);
for row in awsData:
    if row[0] != shared_invoice_number:
        if row[4] == 'n':
            print row[2]
            invoice = Decimal(sub(r'[^\d.]', '',row[3]))
            print invoice
            allocationPercent = Decimal((invoice/nonSharedAmountValue) * Decimal(100.0))
            print "ALLOCATION PERCENTAGE: " + str(allocationPercent)
            sharedAllocationAmount = (sharedAmountValue * allocationPercent) / 100
            auditSharedAllocationAmount = auditSharedAllocationAmount + sharedAllocationAmount
            print "ALLOCATION AMOUNT: " + str(sharedAllocationAmount)
            finalAmount = invoice + sharedAllocationAmount
            print "ORIGINAL AMOUNT:" + str(round(invoice,2))
            print "FINAL AMOUNT:" + str(round(finalAmount,2))
            print "\n"
            for gocrow in gocData:
                if row[1] == gocrow[0]:
                    subAllocationAmount = (finalAmount * Decimal(gocrow[3])) / 100
                    print "SUB ALLOCATION AMOUNT:" + str(round(subAllocationAmount,2))
                    report.write(str(row[0])+ "|" + str(row[1]) + "," + str(row[1]) + "," + str(gocrow[1]) + "," + str(gocrow[2]) + "," + str(gocrow[3]) + "," + str(gocrow[4]) + "," + str(round(subAllocationAmount,2)) +"," + str(row[0]) + "," + str(row[2]) + "\n")

for row in awsData:
    if row[0] != shared_invoice_number:
        if row[4] == 'n':
            print row[2]
            invoice = Decimal(sub(r'[^\d.]', '',row[3]))
            print invoice
            allocationPercent = Decimal((invoice/nonSharedAmountValue) * Decimal(100.0))
            print "ALLOCATION PERCENTAGE: " + str(allocationPercent)
            sharedAllocationAmount = (sharedInvoiceValue * allocationPercent) / 100
            print "ALLOCATION AMOUNT FOR SHARED INVOICE: " + str(sharedAllocationAmount)
            for gocrow in gocData:
                if row[1] == gocrow[0]:
                    subAllocationAmount = (sharedAllocationAmount * Decimal(gocrow[3])) / 100
                    print "SUB ALLOCATION AMOUNT:" + str(round(subAllocationAmount,2))
                    report.write(str(shared_invoice_number)+ "|" + str(row[1]) + "," + str(row[1]) + "," + str(gocrow[1]) + "," + str(gocrow[2]) + "," + str(gocrow[3]) + "," + str(gocrow[4]) + "," + str(round(subAllocationAmount,2)) +"," + str(row[0]) + "," + str(row[2]) + "\n")

report.close()