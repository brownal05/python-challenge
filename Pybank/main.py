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
        minPnlChangeDate = str(date[pnlChange.index(min(pnlChange))])

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", len(date))
    print("Total: $", sum(pnl))
    print("Average Change: $", round(avgPnlChange, 2))
    print("Greatest Increase in Profits: ", maxPnlChangeDate, "( $", int(maxPnlChange), ")")
    print("Greatest Decrease in Profits: ", minPnlChangeDate, "( $", int(minPnlChange), ")")

f = open('output.txt', 'w')   
f.write("Financial Analysis" + '\n')
f.write("----------------------------" + '\n')
f.write("Total Months: " + str(len(date)) + '\n')
f.write("Total: $" + str(sum(pnl)) + '\n')
f.write("Average Change: $" + str(round(avgPnlChange, 2)) + '\n')
f.write("Greatest Increase in Profits: "+ maxPnlChangeDate + "( $" + str(int(maxPnlChange)) + ")" + '\n')
f.write("Greatest Decrease in Profits: "+ minPnlChangeDate + "( $" + str(int(minPnlChange)) + ")" + '\n')
f.close