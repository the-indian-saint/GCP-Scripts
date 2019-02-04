import csv

def getValues():
    compare = {}
    with open ('aws_raw_data_reference.txt', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = '\t')
        for row in csvreader:
            if row[4] == 'y':
                compare[row[1]] = 'yes'
            elif row[4] == 'n':
                compare[row[1]] = 'no'
    #print(compare)
    return compare
    



def createCSV(compare):
    with open ('Monthly_Invoice_2019-01.txt', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter='\t')
        with open ('aws_raw_data.txt', 'w') as new_file:
            fieldnames = ['InvoiceID', 'LinkedAccountId', 'LinkedAccountName', 'TotalCost', 'Shared']
            csvwriter = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
            csvwriter.writeheader()
            for row in csvreader:
                #print(row['LinkedAccountId'])
                if row['LinkedAccountId'] in compare:
                    row['Shared'] = compare[row['LinkedAccountId']]
                    csvwriter.writerow(row)
                else:
                    print(row['LinkedAccountId'] + ' Not Found in aws_raw_data_reference')


compare = getValues()
createCSV(compare)
