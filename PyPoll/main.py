import os
import csv

# csv file path
csvpath = os.path.join('Resources', 'election_data.csv')

# data storing variables
voter_data = []
county_data = []
candidate_data = []

# Open csv file
with open(csvpath) as csvfile:
    # use the reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # grab the header
    csv_header = next(csvreader)

    for row in csvreader:
        voter_data.append(row[0])
        county_data.append(row[1])
        candidate_data.append(row[2])

# Task 1: The total number of votes cast
num_total_votes = len(voter_data)
        
# Task 2: A complete list of candidates who received votes
# get a sorted list of candidates
sorted_candidates = candidate_data
sorted_candidates.sort()

# start off the loop
unique_candidates = [sorted_candidates[0]]
i1 = 0

# loop through sorted candidates, putting into new array if it is not already there
for i in range(1,num_total_votes):
    if sorted_candidates[i] != unique_candidates[i1]:
        i1 += 1
        unique_candidates.append(sorted_candidates[i])

        
# Task 3 + 4: The percentage of votes each candidate won, the total number of votes each candidate won
# create dictionary for each candidate
# code gotten from: https://stackoverflow.com/questions/30280856/populating-a-dictionary-using-two-for-loops-in-python
candidate_dict = {}
for i in range(len(unique_candidates)):
    candidate_dict[unique_candidates[i]] = 0

# loop through each voter
# this is the total number of votes for each candidate
for i in range(num_total_votes):
    candidate_dict[candidate_data[i]] += 1

# percentage will be calculated as part of printing

        
        
# Task 5: The winner of the election based on popular vote
max_votes = 0
winner = ""
for i in range(len(unique_candidates)):
    if candidate_dict[unique_candidates[i]] > max_votes:
        max_votes = candidate_dict[unique_candidates[i]]
        winner = unique_candidates[i]


# Set up printing strings
out_strings = ["Election Results\n-------------------------",
               f"Total Votes: %s" % (num_total_votes),
               "-------------------------"]
for i in range(len(unique_candidates)):
    curr_vote = candidate_dict[unique_candidates[i]]
    out_strings.append(f"%s: %.3f%% (%s)" % (unique_candidates[i], curr_vote/num_total_votes*100, curr_vote))

out_strings.append("-------------------------")
out_strings.append(f"Winner: %s" % winner)
out_strings.append("-------------------------")

# PRINTING to terminal
print("")
for i in range(len(out_strings)):
    print(out_strings[i])
print("")

# PRINTING to file
output_path = os.path.join('analysis', 'PyPoll.txt')
with open(output_path, 'w') as txtfile:
    for i in range(len(out_strings)):
        txtfile.write(out_strings[i]+"\n")







