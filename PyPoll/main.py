# Import os module to create file paths across operating systems
import os

# Import module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Set variables
vote_counter = 0
candidates = []
candidate_votes = []
candidate_data = {}

# Read cvs file
with open(csvpath) as csvfile:

     # Specify delimiter and variable that holds contents
     csvreader = csv.reader(csvfile, delimiter=',')

     # Skip first row
     next(csvreader)

     # Read each row of data
     for row in csvreader:

        # Count the total number of votes
        vote_counter = vote_counter + 1

        # # Determine list of candidates
        if row[2] not in candidate_data:
        	candidate_data[row[2]] = 0

        # if row[2] not in candidates:
        # 	candidates.append(row[2])
        # 	candidate_votes.append(0)
        
        # Calculate the total number of votes each candidate won
        candidate_data[row[2]] += 1

        # index = candidates.index(row[2])
        # candidate_votes[index] += 1

print("Election Results")
print("-------------------------")

# Print the total number of votes cast
print("Total Votes: ", vote_counter,sep='')

print("-------------------------")

# Print the list of candidates along with the percentage of and total number of votes won
# Calculate the percentage of votes each candidate won

for k, v in candidate_data.items():
    print(k,": ",round(((v/vote_counter)*100),3),"% ","(",v,")",sep='')

# votes = 0
# for candidate in candidates:
# 	print(candidate,": ", round(((candidate_votes[votes]/vote_counter)*100),3),"% ","(",candidate_votes[votes],")",sep='')
# 	votes += 1

print("-------------------------")

# The winner of the election based on popular vote
print(max(candidate_data, key=candidate_data.get))

# winner = candidate_votes.index(max(candidate_votes))

# print(candidates[winner])
print("-------------------------")
