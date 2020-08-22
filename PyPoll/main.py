import os
import csv
import sys

csv_path = os.path.join("H:/RICEBOOTCAMP/Homework/python-challenge/PyPoll/Resources/election_data.csv")

with open(csv_path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter = ',')
    
    header = next(reader)

    totalVotes = 0
  
    candidates = []

    votes = []
    for rows in reader:


        totalVotes +=1

        if rows[2] not in candidates:
            
            candidates.append(rows[2])
            votes.append(1)

        else:
            candidate_index = candidates.index(rows[2])
            votes[candidate_index] +=1

    MostVotes = 0
    Winner = []
    Percentages = []
    for vote in range(len(votes)):

        percent = round((votes[vote] / totalVotes)*100, 2)
        Percentages.append(percent)

        if votes[vote] > MostVotes:
            MostVotes = votes[vote]
            Winner.append(candidates[vote])


        
print(votes)
print(Winner)
print(f"Total Votes: {totalVotes}")
print(Percentages)

