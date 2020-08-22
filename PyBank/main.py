import os
import csv
import sys

csv_path = os.path.join("H:/RICEBOOTCAMP/Homework/python-challenge/PyBank/Resources/budget_data.csv")
#csv_path = os.path.join("..", "Resources", "budget_data.csv")

with open(csv_path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter = ',')
    
    header = next(reader)

    print(header)

    TotalMonths = 0
    
    ## Initialize the change in profit
    ProfitChangeInitial = 0

    ProfitLossInitial = 0

    TotalProfitLoss = 0
    
    ProfitChange = []
    
    ProfitInitial = 0
    
    for rows in reader:

        TotalMonths +-1
        
        
        Profit = float(rows[1])
        TotalProfitLoss = TotalProfitLoss + Profit
       
        ## Create a list of all profit deltas
        ProfitChangeCurrent = Profit - ProfitInitial
        ProfitChange.append(ProfitChangeCurrent)
        ProfitInitial = Profit

        if ProfitChangeCurrent > ProfitChangeInitial:

            ProfitChangeInitial = ProfitChangeCurrent
            GreatestMonth = rows[0]
        if ProfitChangeCurrent < ProfitLossInitial:
            ProfitLossInitial = ProfitChangeCurrent
            WorstMonth = rows[0]
           



    ##Ignore first delta 
    ProfitChangeNew = (ProfitChange[1:(len(ProfitChange))])
    TotalChange = sum(ProfitChangeNew)
    AverageChange = TotalChange / (len(ProfitChangeNew))
    
    
    print("Financial Analysis")
    print("-"*40)
    print(f"Total Months: {TotalMonths}")
    print(f"Total Profit/Loss: {TotalProfitLoss}")
    
    print(f"Average Change: {AverageChange}")
   

    print(f"Greatest Increase in Profits: {GreatestMonth} ({ProfitChangeInitial})")
    print(f"Greatest Decrease in Profits: {WorstMonth} ({ProfitLossInitial})")

    sys.stdout = open("PyBank/Analysis/analysis.txt", "w")
    
    print("Financial Analysis")
    print("-"*40)
    print(f"Total Months: {TotalMonths}")
    print(f"Total Profit/Loss: {TotalProfitLoss}")
    
    print(f"Average Change: {AverageChange}")
   

    print(f"Greatest Increase in Profits: {GreatestMonth} ({ProfitChangeInitial})")
    print(f"Greatest Decrease in Profits: {WorstMonth} ({ProfitLossInitial})")

    sys.stdout.close()

    

