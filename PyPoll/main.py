import os
import csv
totalVotes = []
pollcsv = os.path.join('Resources', "election_data.csv" )
    
Candidate = {}
Votes = 0
         
with open(pollcsv, newline = '') as pollfile:
    reader = csv.reader(pollfile, delimiter=',')
    next(reader)
    for row in reader:
        if row[2] not in Candidate:
            Candidate[row[2]]=1
        else:
            Candidate[row[2]]= Candidate.get(row[2]) + 1
        Votes = Votes + 1 
    print("Election Results", '\n', "------------------------", '\n', "Total Votes: ", str(Votes), '\n', "------------------------",'\n')
  
    for key in Candidate:
       print(f'{key}: {round((Candidate[key]/Votes)*100)}% ({Candidate[key]})')
    print("------------------------")
    print("Winner: " + str(max(Candidate, key=Candidate.get)))
    print("------------------------")

    f = open('output.txt','w')
    f.write("Election Results" + '\n' + "------------------------" + '\n' "Total Votes: "+str(Votes) + '\n'+ ("------------------------") + '\n' )
    for key in Candidate:
       f.write(f'{key}: {round((Candidate[key]/Votes)*100)}% ({Candidate[key]})' + '\n ')
    f.write("------------------------" + '\n' + "Winner: " + str(max(Candidate, key=Candidate.get)) + '\n' + "------------------------" + '\n')
    
   