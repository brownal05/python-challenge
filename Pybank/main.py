import os
import csv

bank_file = os.path.join("", "Resources", "budget_data.csv")
with open(bank_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")    
    row_count = sum(1 for row in csvfile) 
    #print(sum(int(x[1]) for x in csvreader))
    
print(row_count)


