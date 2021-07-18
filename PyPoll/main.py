import os
import csv
from typing import TYPE_CHECKING

election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")
file_to_output = os.path.join("PyPoll", "Resources", "election_results.txt")

# Variables

total_votes = 0
#khan_percent = 0
#khan_sum = 0
#correy_sum = 0
#correy_percent = 0
#li_sum = 0
#li_percent = 0
#otooley_sum = 0
#otooley_percent = 0

candidate_name = []
winner = ""
can_votes = {}
can_percent = 0




with open(election_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    header = next(csv_reader)
    for row in csv_reader:
        #Summing the votes
        total_votes += 1

        #Extracting candidate name
        can_name = row[2]
        if can_name not in candidate_name:
            candidate_name.append(can_name)
            can_votes[can_name] = 0
        
        can_votes[can_name]= can_votes[can_name]+1

             ###use .get() to get votes for current candidate
    khan_results = can_votes.get("Khan")
    correy_results = can_votes.get("Correy")
    li_results = can_votes.get("Li")
    otooley_results = can_votes.get("O'Tooley")

    khan_cent = round(khan_results / total_votes, 3) * 100
    correy_cent = round(correy_results / total_votes, 3) * 100
    li_cent = round(li_results / total_votes, 3) * 100
    otooley_cent = round(otooley_results / total_votes, 3) * 100
   

with open(file_to_output, "w") as txt_file:
    election_results = (
      f"\n\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes}\n"
      f"-------------------------\n"
      f"Khan: {khan_cent} ({khan_results})\n"
      f"Khan: {correy_cent} ({correy_results})\n"
      f"Li: {li_cent} ({li_results})\n"
      f"O'Tooley: {otooley_cent} ({otooley_results})\n")

    print(election_results, end="")
    txt_file.write(election_results)

    ## loop over can_votes
    
     ###use .get() to get votes for current candidate
    #khan_results = can_votes.get("Khan")

    #khan_cent = round(khan_results / total_votes, 3) * 100
    #print(f'Khan: {khan_cent} {khan_results}')


    #### calculate percentage here   

