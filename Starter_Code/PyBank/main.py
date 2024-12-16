# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_sum = 0
net_change_total = 0
previous_profit = None
greatest_increase = float('-inf')  # Start with the lowest possible value
greatest_decrease = float('inf')    # Start with the highest possible value
month_list = []
greatest_increase_month = ""
greatest_decrease_month = ""

# Open and read the csv
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data, delimiter=",")

    # Skip the header row
    next(reader)

    # Process each row of data
    for row in reader:
        month_list.append(row[0])
        current_profit = int(row[1])
        
        # Add current month's profit into total sum
        total_sum += current_profit

        # Calculate the net change and track it
        if previous_profit is not None:  # Skip the first month since there's no previous profit
            net_change = current_profit - previous_profit
            net_change_total += net_change

            # Calculate the greatest increase in profits (month and amount)
            if net_change > greatest_increase:
                greatest_increase = net_change
                greatest_increase_month = row[0]

            # Calculate the greatest decrease in losses (month and amount)
            if net_change < greatest_decrease:
                greatest_decrease = net_change
                greatest_decrease_month = row[0]

        # Update previous profit for next iteration
        previous_profit = current_profit

# Calculate the average net change across the months
average_change = net_change_total / (len(month_list) - 1) if len(month_list) > 1 else 0
formatted_average_change = "${:.2f}".format(average_change)

# Generate the output summary
print("Financial Analysis")
print("----------")
print("The total number of months is:", len(month_list))
print("Total: $", total_sum)
print("The average change is:", formatted_average_change)
print("The greatest increase in profits:", greatest_increase_month, "$", greatest_increase)
print("The greatest decrease in profits:", greatest_decrease_month, "$", greatest_decrease)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------\n")
    txt_file.write(f"The total number of months is: {len(month_list)}\n")
    txt_file.write(f"Total: ${total_sum}\n")
    txt_file.write(f"The average change is: {formatted_average_change}\n")
    txt_file.write(f"The greatest increase in profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write(f"The greatest decrease in profits: {greatest_decrease_month} (${greatest_decrease})\n")