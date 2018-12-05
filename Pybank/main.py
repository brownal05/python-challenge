import os
import csv

csvpath = os.path.join("", "Resources", "budget_data.csv")
print(csvpath)
# 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")     
    for months in csvreader:
        row_count =  
       #sum(1 for months in csvfile))
        print("Number of months: " + str(row_count)) 
#    yr_pl_sum = sum(row[1])
#    print("Total Profit/Loss: " + str(yr_pl_sum)) 


