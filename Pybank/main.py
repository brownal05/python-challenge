import os
import csv

#open csv
bank_file = os.path.join("", "Resources", "budget_data.csv")
Change = []

MyList = []
#count the rows
with open(bank_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")    
    RowCount = sum(1 for row in csvfile) 
#P/L calculation
with open(bank_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    BankList = list(csvreader)
    #print(sum(int(x[1]) for x in csvreader))
    Profits = sum(int(row[1]) for row in BankList)
#Avg change between months
with open(bank_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    BankList = list(csvreader)   
    PrevRev = 0

    for row in BankList:
        
        Change =  int(row[1]) - PrevRev 
        PrevRev = int(row[1])
        MyList.append(Change)
        
print(MyList)
print(RowCount)
print(str(Profits))
print(str(Change))
