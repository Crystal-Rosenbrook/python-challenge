import os
import csv

# Define the path for the input file
csvpath = r"C:\Users\cryst\Documents\UMN Data Visualization and Analytics Bootcamp\Coursework\Section 2 Data Analytics with Python\Module 3\Challenge Files\Starter_Code\PyBank\Resources\budget_data.csv"

# Initialize variables
months = []
profit_losses = []
changes = []

# Open the input file
with open(csvpath, newline='') as csvfile:

    # Read the input file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Loop through the data and store in the lists
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

# Calculate the total number of months and the net total amount of "Profit/Losses"
total_months = len(months)
net_total = sum(profit_losses)

# Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
for i in range(1, len(profit_losses)):
    changes.append(profit_losses[i] - profit_losses[i-1])
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits and their corresponding dates
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

# Print the results
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Define the path for the output file
output_file = r"C:\Users\cryst\Documents\UMN Data Visualization and Analytics Bootcamp\Coursework\Section 2 Data Analytics with Python\Module 3\Challenge Files\Starter_Code\PyBank\Resources\budget_analysis.txt"

# Export the results to a text file
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("---------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}\n)")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")