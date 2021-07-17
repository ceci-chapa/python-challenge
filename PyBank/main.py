import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Variables

total_months = 0
total = 0
average_change = 0
average_change_list = []
previous_profit = 0
greatest_increase = []
greatest_decrease = []


with open(budget_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    header = next(csv_reader)
    for row in csv_reader:
        net_change = previous_profit - int(row[1])
        previous_profit = int(row[1])

        #Summing the months
        total_months += 1
        
        #Adding the total months
        total = total + int(row[1]) 

        #Calculating the average change
        average_change_list.append(net_change)

    average_change = sum(average_change_list) / (len(average_change_list) - 1)

    print("Financial Analysis")
    print("----------------------------")
    print(total_months)
    print(total)
    print(average_change)

