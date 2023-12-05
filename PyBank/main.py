# Import os module to create file paths across operating systems
import os

# Import module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Set variables
month_counter = 0
net_profit_loss = 0
greatest_increase_profits = 0
greatest_increase_month = ""
greatest_decrease_profits = 0
greatest_decrease_month = ""
previous_month_revenue = 0
current_revenue_change = 0
total_revenue_change = 0

# Read cvs file
with open(csvpath) as csvfile:

     # Specify delimiter and variable that holds contents
     csvreader = csv.reader(csvfile, delimiter=',')

     # Skip first row
     next(csvreader)

     #Set variable for first month
     first_month = 0     

     # Read each row of data after the header
     for row in csvreader:

        # Count the total number of months included in the dataset    
        month_counter = month_counter + 1
     
        # Calculate the net total amount of "Profit/Losses" over the entire period
        net_profit_loss += int(row[1])

        # Added revenue change over the entire period
        current_revenue_change = int(row[1]) - previous_month_revenue
        total_revenue_change += current_revenue_change
        if first_month == 0:
            first_month = current_revenue_change

        # Calculate greatest increase in profits over the entire period
        if current_revenue_change > greatest_increase_profits:
            greatest_increase_profits = current_revenue_change
            greatest_increase_month = row[0]

        # Calculate greatest decrease in profits over the entire period
        if current_revenue_change < greatest_decrease_profits:
            greatest_decrease_profits = current_revenue_change
            greatest_decrease_month = row[0]

        previous_month_revenue = int(row[1])


print("Financial Analysis")
print("----------------------------")

# Print the number of months in the dataset
print("Total Months: ", month_counter,sep='')

# Print the net total amount of "Profit/Losses" over the entire period
print("Total: ","$",net_profit_loss,sep='')

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
print("Average Change: ","$",round((total_revenue_change - first_month)/(month_counter - 1),2),sep='')

# Print the greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: ",greatest_increase_month," ($",greatest_increase_profits,")",sep='')

# Print the greatest decrease in profits (date and amount) over the entire period
print("Greatest Decrease in Profits: ",greatest_decrease_month," ($",greatest_decrease_profits,")",sep='')


#Export text file with results
file = 'analysis/budget_data_analysis.txt'
with open(file, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write("Total Months: " + str(month_counter))
    output.write("\n")
    output.write("Total: $" + str(net_profit_loss))
    output.write("\n")
    output.write("Average Change: $" + str(round((total_revenue_change - first_month)/(month_counter - 1),2)))
    output.write("\n")
    output.write("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase_profits) +")\n")
    output.write("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease_profits) +")")
