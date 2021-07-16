import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data
title = []
total_months = []
total = []
average_change = []
greatest_increase = []
greatest_decrease = []

with open(budget_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    for row in csv_reader:

        #Adding the title
        title.append(row[0]) = "Financial Analysis"

        #Adding the total months
        



