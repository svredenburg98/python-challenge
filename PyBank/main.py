import os
import csv

csv_path = os.path.join("H:/RICEBOOTCAMP/Homework/python-challenge/PyBank/Resources/budget_data.csv")

with open(csv_path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter = ',')
    
    header = next(reader)

    print(header)

    TotalMonths = 0
    
    TotalProfitLoss = 0
    ProfitChange = []
    for rows in reader:

        TotalMonths += 1
        Profit = float(rows[1])
        TotalProfitLoss = TotalProfitLoss + Profit
        

    print("Financial Analysis")
    print("-"*40)
    print(f"Total Months: {TotalMonths}")
    print(f"Total Profit/Loss: {TotalProfitLoss}")
    

