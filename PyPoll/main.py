import os
import csv
from typing import TYPE_CHECKING

election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Variables

total_votes = 0
khan_percent = 0
khan_sum = 0
correy_sum = 0
correy_percent = 0
li_sum = 0
li_percent = 0
otooley_sum = 0
otooley_percent = 0

candidate_list = []



with open(election_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    header = next(csv_reader)
    for row in csv_reader:

        #Finding the totals for each candidate
        if row[2]  == "Khan":
            khan_sum += 1
        
        if row[2] == "Correy":
            correy_sum += 1

        if row[2] == "Li":
            li_sum += 1

        if row[2] == "O'Tooley":
            otooley_sum += 1

        #add an if statment here for the winner 

        #Summing the votes
        total_votes += 1

    print(total_votes)
    print(khan_sum)
    print(correy_sum)
    print(li_sum)

