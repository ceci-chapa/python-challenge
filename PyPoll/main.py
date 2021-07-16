import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_csv, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    print("Hello")