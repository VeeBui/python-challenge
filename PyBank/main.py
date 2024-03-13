import os
import csv

# csv file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# data storing variables
month_data = []
profit_data = []

# Open csv file
with open(csvpath) as csvfile:
    # use the reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # grab the header
    csv_header = next(csvreader)

    for row in csvreader:
        month_data.append(row[0])
        profit_data.append(int(row[1]))

# Task 1: The total number of months included in the dataset
num_total_months = len(month_data)

# Task 2: The net total amount of "Profit/Losses" over the entire period
total_profit_loss = sum(profit_data)

# Task 3: The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = 0
# Task 4: The greatest increase in profits (date and amount) over the entire period
greatest_inc = profit_data[0]
greatest_inc_mon = month_data[0]
# Task 5: The greatest decrease in profits (date and amount) over the entire period
greatest_dec = profit_data[0]
greatest_dec_mon = month_data[0]

for i in range(1,num_total_months):
    # get change in profit
    curr_change = profit_data[i] - profit_data[i-1]

    # total up changes
    changes += curr_change

    # check if new greatest increase
    if curr_change > greatest_inc:
        greatest_inc = curr_change
        greatest_inc_mon = month_data[i]

    # check if new greatest decrease
    if curr_change < greatest_dec:
        greatest_dec = curr_change
        greatest_dec_mon = month_data[i]

# get average change for Task 3
average_change = changes/(num_total_months-1)

# Set up printing strings
out_strings = ["Financial Analysis\n----------------------------",
               f"Total Months: {num_total_months}",
               f"Total: $%.0f" % total_profit_loss,
               f"Average Change: $%.2f" % average_change,
               f"Greatest Increase in Profits: %s $(%.0f)" % (greatest_inc_mon, greatest_inc),
               f"Greatest Decrease in Profits: %s $(%.0f)" % (greatest_dec_mon, greatest_dec)]

# PRINTING to terminal
print("")
for i in range(len(out_strings)):
    print(out_strings[i])
print("")

# PRINTING to file
output_path = os.path.join('analysis', 'PyBank.txt')
with open(output_path, 'w') as txtfile:
    for i in range(len(out_strings)):
        txtfile.write(out_strings[i]+"\n")




