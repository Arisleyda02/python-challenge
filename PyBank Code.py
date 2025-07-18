"""PyBank Homework Starter File."""
# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
monthly_changes = []
profit_changes_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")
    
    # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to profit_changes_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    # Process each row of data
    for row in reader:
        total_months += 1
        total_net += int(row[1])
        
        # Calculate net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        profit_changes_list.append(net_change)
        monthly_changes.append(row[0])
        
        # Check for greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]
        
        # Check for greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average net change across the months
average_net_change = sum(profit_changes_list) / len(profit_changes_list)

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
os.makedirs(os.path.dirname(file_to_output), exist_ok=True)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
# python-challenge