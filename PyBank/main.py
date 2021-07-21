import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Resources", "financial_analysis.txt")

# Variables

total_months = 0
total = 0
average_change = 0
average_change_list = []
previous_profit = 0
greatest_increase = ["", 0]
greatest_decrease = ["",0]


#Reading the csv file
with open(budget_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    header = next(csv_reader)
    #This first_row will help the loop start on the correct row to being calculations
    first_row = next(csv_reader)

    #Amounts need to be calculated before the loop to get the correct totals
    total_months += 1
    total += int(first_row[1])
    previous_profit = int(first_row[1])

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

#Exporting the text files
with open(file_to_output, "w") as txt_file:
    financial_anlysis = (
      f"\n\nFinancial Analysis\n"
      f"-------------------------\n"
      f"Total Months: {total_months}\n"
      f"Total: ${total}\n"
      f"Average Change: ${average_change}\n"
      f"Greatest Increase: {greatest_increase[0]} " f"(${greatest_increase[1]})\n"  
      f"Greatest Decrease: {greatest_decrease[0]} " f"(${greatest_decrease[1]})\n"
      )

    print(financial_anlysis, end="")
    txt_file.write(financial_anlysis)

