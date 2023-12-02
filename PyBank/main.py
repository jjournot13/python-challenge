# Import os module to create file paths across operating systems
import os

# Import module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Read cvs file
with open(csvpath) as csvfile:

     # CSV reader specifies delimiter and variable that holds contents
     csvreader = csv.reader(csvfile, delimiter=',')

     print(csvreader)

     # Read the header row first (skip this step if there is no header)
#     csv_header = next(csvreader)
#     print(f"CSV Header: {csv_header}")

#     # Read each row of data after the header
#     for row in csvreader:
#         print(row)


# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Print
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558) -->