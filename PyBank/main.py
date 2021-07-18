import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")
file_to_output = os.path.join("PyBank", "Resources", "financial_analysis.txt")

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

with open(file_to_output, "w") as txt_file:
    financial_anlysis = (
      f"\n\nFinancial Analysis\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes}\n"
      f"-------------------------\n"
      f"Khan: {khan_cent} ({khan_results})\n"
      f"Khan: {correy_cent} ({correy_results})\n"
      f"Li: {li_cent} ({li_results})\n"
      f"O'Tooley: {otooley_cent} ({otooley_results})\n"
      f"-------------------------\n"
      f"Winner: \n"
      f"-------------------------\n")

    print(financial_anlysis, end="")
    txt_file.write(financial_anlysis)

