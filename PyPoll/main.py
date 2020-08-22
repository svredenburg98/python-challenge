import os
import csv
import sys

csv_path = os.path.join("H:/RICEBOOTCAMP/Homework/python-challenge/PyPoll/Resources/election_data.csv")

with open(csv_path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter = ',')
    
    header = next(reader)

    totalVotes = 0
    vote1=0
    vote2=0
    vote3=0
    vote4=0
    votepercents = []
   
    candidates = []
    for rows in reader:


        totalVotes +=1

        if rows[2] not in candidates:
            
            candidates.append(rows[2])

        
        if rows[2] == candidates[0]:
            vote1 +=1
        elif rows[2] == candidates[1]:
            vote2 +=1
        elif rows[2] == candidates[2]:
            vote3 +=1
        elif rows[2] == candidates[3]:
            vote4 +=1
        
    votecounts = [vote1, vote2, vote3, vote4]
    
    for count in votecounts:
        percent = round(((count/totalVotes)*100), 2)
        votepercents.append(percent)
        

        

print(f"Total Votes: {totalVotes}")
print(f" {candidates[0]}: {votepercents[0]}% ({vote1})")
print(f" {candidates[1]}: {votepercents[1]}% ({vote2})")
print(f" {candidates[2]}: {votepercents[2]}% ({vote3})")
print(f" {candidates[3]}: {votepercents[3]}% ({vote4})")
print(votecounts)
print(votepercents)
