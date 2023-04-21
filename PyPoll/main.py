import os
import csv

# Define the path for the input file
csvpath = r"C:\Users\cryst\Documents\UMN Data Visualization and Analytics Bootcamp\Coursework\Section 2 Data Analytics with Python\Module 3\Challenge Files\Starter_Code\PyPoll\Resources\election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner_votes = 0
winner = ""

# Open the input file
with open(csvpath, newline='') as csvfile:
    
    # Read the input file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
        
        # Count the total number of votes cast
        total_votes += 1
        
        # Count the number of votes for each candidate
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1
            
# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Initialize the output string
output_string = "Election Results\n"
output_string += "-------------------------\n"
output_string += f"Total Votes: {total_votes}\n"
output_string += "-------------------------\n"

# Loop through the candidates
for candidate_name in candidates:
    
    # Calculate the percentage of votes
    candidate_votes = candidates[candidate_name]
    candidate_percentage = candidate_votes / total_votes * 100
    
    # Print the candidate results to the terminal
    print(f"{candidate_name}: {candidate_percentage:.3f}% ({candidate_votes})")
    
    # Update the winner if needed
    if candidate_votes > winner_votes:
        winner_votes = candidate_votes
        winner = candidate_name
        
    # Append the candidate results to the output string
    output_string += f"{candidate_name}: {candidate_percentage:.3f}% ({candidate_votes})\n"
    
# Print the winner to the terminal
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Append the winner to the output string
output_string += "-------------------------\n"
output_string += f"Winner: {winner}\n"
output_string += "-------------------------\n"

# Define the path for the output file
output_file = r"C:\Users\cryst\Documents\UMN Data Visualization and Analytics Bootcamp\Coursework\Section 2 Data Analytics with Python\Module 3\Challenge Files\Starter_Code\PyPoll\Resources\election_analysis.txt"

# Export the results to a text file
with open(output_file, "w") as textfile:
    textfile.write(output_string)