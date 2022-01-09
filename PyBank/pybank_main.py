import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0
profit_loss = []


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        total_months += 1
        profit_loss.append(int(row[1]))
    
    profit_loss_total = sum(profit_loss)
    max_profit_increase = max(profit_loss)
    min_profit_increase = min(profit_loss)


    print("Financial Analysis")
    print("--------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + str(profit_loss_total))
    print("Greatest profit increase: " + str(max_profit_increase))
    print("Greatest profit loss: " + str(min_profit_increase))
