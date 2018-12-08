import os
import csv

#open csv
bank_file = os.path.join("", "Resources", "budget_data.csv")
pnlChange = []
pnl = []
date = []


with open(bank_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    next(csvreader)
    #print(f"CSV Header: {csv_header}") 
    for row in csvreader:
        
        date.append(row[0])
        pnl.append(float(row[1]))
    for i in range(1, len(pnl)):
        pnlChange.append(pnl[i] - pnl[i-1])
        avgPnlChange = sum(pnlChange)/len(pnlChange)
        maxPnlChange = max(pnlChange)
        minPnlChange = min(pnlChange)
        maxPnlChangeDate = str(date[pnlChange.index(max(pnlChange))])
        minPnlChangeDate = str(date[pnlChange.index(max(pnlChange))])

print("Financial Analysis")
print("----------------------------")
print("Total Months: ", len(date))
print("Total: $", sum(pnl))
print("Average Change: $", avgPnlChange)