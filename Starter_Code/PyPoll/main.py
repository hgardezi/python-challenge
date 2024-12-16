# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
Candidates_options = []
Candidates_dict = {}

# Winning Candidate and Winning Count Tracker
winning_total = 0
winning_candidate = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")
    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1
        
        # Get the candidate’s name from the row
        candidate_name = row[2]
        
        # If the candidate is not already in the candidate list, add them
        if candidate_name not in Candidates_options:
            Candidates_options.append(candidate_name)
            Candidates_dict[candidate_name] = 0
        
        # Add a vote to the candidate’s count
        Candidates_dict[candidate_name] += 1

# Determine the winning candidate by counting votes in dictionary
for key in Candidates_dict.keys():
    if Candidates_dict[key] > winning_total:
        winning_candidate = key
        # Determine the winning total number of votes
        winning_total = Candidates_dict[key]

# Calculate the percentages for each candidate and format them as percentages
Percentage_formats = {}
for candidate in Candidates_options:
    percentage = (Candidates_dict[candidate] / total_votes) * 100
    Percentage_formats[candidate] = f"{percentage:.3f}%"

# Convert integers to strings so they can be written in .txt file
total_votes_str = str(total_votes)

# Generate and print the winning candidate summary in terminal
print(Candidates_dict)
print("Election Results")
print("----------")
print("Total Votes:", total_votes_str)
print("----------")
for candidate in Candidates_options:
    print(f"{candidate}: {Percentage_formats[candidate]} | Vote Total: {Candidates_dict[candidate]}")
    print("----------")
    print("Winner:", winning_candidate)
    print("----------")
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("----------\n")
    txt_file.write(f"{Candidates_options[0]}: {Percentage_formats[Candidates_options[0]]} | Vote Total: {Candidates_dict[Candidates_options[0]]}\n")
    txt_file.write(f"{Candidates_options[1]}: {Percentage_formats[Candidates_options[1]]} | Vote Total: {Candidates_dict[Candidates_options[1]]}\n")
    txt_file.write(f"{Candidates_options[2]}: {Percentage_formats[Candidates_options[2]]} | Vote Total: {Candidates_dict[Candidates_options[2]]}\n")
    txt_file.write("----------\n")
    txt_file.write(f"Winner:, {winning_candidate}\n")