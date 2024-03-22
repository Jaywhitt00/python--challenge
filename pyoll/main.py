import os
import csv

election_data= os.path.join("Resources", "election_data.csv")
# Initialize variables
total_votes = 0
candidates = {}
    
# Read the CSV file and analyze the votes
with open("election_data.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_votes += 1
            candidate = row['Candidate']
            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1
    
# Calculate percentage of votes for each candidate
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}
    
# Find the winner
winner = max(candidates, key=candidates.get)
    
# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("Candidates who received votes:")
for candidate, votes in candidates.items():
        print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")





