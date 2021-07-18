import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Variables

total_months = 0
total = 0
average_change = 0
average_change_list = []
previous_profit = 0
greatest_increase = ["", 0]
greatest_decrease = ["",0]


with open(budget_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    header = next(csv_reader)
    for row in csv_reader:
        net_change = int(row[1]) - previous_profit
        previous_profit = int(row[1])

        if net_change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change   


        #Summing the months
        total_months += 1
        
        #Adding the total months
        total = total + int(row[1]) 

        #Calculating the average change
        average_change_list.append(net_change)

    average_change = round(sum(average_change_list) / (len(average_change_list)),2)

    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {total_months}')
    print(total)
    print(average_change)
    print(greatest_increase)
    print(greatest_decrease)

