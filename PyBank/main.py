import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data

total_months = 0
total = 0
average_change = 0
average_change_list = []
previous_profit = 0
greatest_increase = []
greatest_decrease = []


with open(budget_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Read the header
    header = next(csv_reader)
    for row in csv_reader:
        net_change = row[1] - previous_profit
        previous_profit = row[1]

        #Adding the title
        total_months += 1

        #Adding the total months
        total = total + row[1] 

        #Calculating the average change
        average_change_list.append(net_change) 
        average_change = 

        



