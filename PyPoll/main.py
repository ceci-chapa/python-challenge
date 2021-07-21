import os
import csv
from typing import TYPE_CHECKING

election_csv = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Resources", "election_results.txt")

# Variables

total_votes = 0


candidate_name = []
winner = ""
can_votes = {}
can_percent = 0



#Reading the csv file
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

    #For loop to pull the winner
    #Using winner_vote to set the variable to 0 to check the max as it loops

    winner_vote = 0
    for name, votes in can_votes.items():

        if votes > winner_vote:
            winner_vote = votes
            winner = name  

    #Using .get() to get votes for current candidate
    khan_results = can_votes.get("Khan")
    correy_results = can_votes.get("Correy")
    li_results = can_votes.get("Li")
    otooley_results = can_votes.get("O'Tooley")

    #Getting the percentages
    khan_cent = "{:.3f}%".format(khan_results / total_votes * 100)
    correy_cent = "{:.3f}%".format(correy_results / total_votes * 100)
    li_cent = "{:.3f}%".format(li_results / total_votes * 100)
    otooley_cent = "{:.3f}%".format(otooley_results / total_votes * 100)
   
#Exporting the textfile
with open(file_to_output, "w") as txt_file:
    election_results = (
      f"\n\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes}\n"
      f"-------------------------\n"
      f"Khan: {khan_cent} ({khan_results})\n"
      f"Correy: {correy_cent} ({correy_results})\n"
      f"Li: {li_cent} ({li_results})\n"
      f"O'Tooley: {otooley_cent} ({otooley_results})\n"
      f"-------------------------\n"
      f"Winner: {winner}\n"
      f"-------------------------\n")

    print(election_results, end="")
    txt_file.write(election_results)



