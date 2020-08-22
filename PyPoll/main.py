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



print("Election Results")
print("-"*30)
print("Total Votes: " + str(totalVotes))
print("-"*30)
print(f"{candidates[0]}: {Percentages[0]}% ({votes[0]})")
print(f"{candidates[1]}: {Percentages[1]}% ({votes[1]})")
print(f"{candidates[2]}: {Percentages[2]}% ({votes[2]})")
print(f"{candidates[3]}: {Percentages[3]}% ({votes[3]})")
print("-"*30)
print("Winner: " + str(Winner[0]))

sys.stdout = open("PyPoll/Analysis/vote_analysis.txt", "w")
    
print("Election Results")
print("-"*30)
print("Total Votes: " + str(totalVotes))
print("-"*30)
print(f"{candidates[0]}: {Percentages[0]}% ({votes[0]})")
print(f"{candidates[1]}: {Percentages[1]}% ({votes[1]})")
print(f"{candidates[2]}: {Percentages[2]}% ({votes[2]})")
print(f"{candidates[3]}: {Percentages[3]}% ({votes[3]})")
print("-"*30)
print("Winner: " + str(Winner[0]))

sys.stdout.close()