import os
import csv

csv_path = os.path.join("H:/RICEBOOTCAMP/Homework/python-challenge/PyBank/Resources/budget_data.csv")

with open(csv_path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter = ',')
    
    header = next(reader)

    print(header)

    TotalMonths = 0
    #Months = []
    ## Initialize the change in profit
    ProfitChangeInitial = 0

    TotalProfitLoss = 0
    
    ProfitChange = []
    
    ProfitInitial = 0
    
    for rows in reader:

        TotalMonths +-1
        
        #Months.append(rows[0])
        Profit = float(rows[1])
        TotalProfitLoss = TotalProfitLoss + Profit
       
        ## Create a list of all profit deltas
        ProfitChangeCurrent = Profit - ProfitInitial
        ProfitChange.append(ProfitChangeCurrent)
        ProfitInitial = Profit

        if ProfitChangeCurrent > ProfitChangeInitial:
            #GreatestIncreaseValue = ProfitChangeCurrent
            #GreatestIncreaseMonth = rows[0]
            ProfitChangeInitial = ProfitChangeCurrent
            GreatestMonth = rows[0]
        #elif ProfitChangeCurrent < ProfitChangeInitial:
            #GreatestLossValue = ProfitChangeCurrent
            #GreatestLossMonth = rows[0]
           



    ##Ignore first delta 
    ProfitChangeNew = (ProfitChange[1:(len(ProfitChange))])
    TotalChange = sum(ProfitChangeNew)
    AverageChange = TotalChange / (len(ProfitChangeNew))
    #MonthChange = dict(zip(Months, ProfitChange))
    #ProfitChangeNew.sort()
    print("Financial Analysis")
    print("-"*40)
    print(f"Total Months: {TotalMonths}")
    print(f"Total Profit/Loss: {TotalProfitLoss}")
    #print(ProfitChange)
    print(f"Average Change: {AverageChange}")
    #print(f"Greatest Increase: {ProfitChangeNew[len(ProfitChangeNew) -1]}")
    #print(f"Greatest Decrease: {ProfitChangeNew[0]}")
    #print(MonthChange)
    print(f"Greatest Increase in Profits: {GreatestMonth} ({ProfitChangeInitial})")
    

