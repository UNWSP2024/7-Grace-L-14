'''Rainfall Program
By Grace LeVoir
3 - 5 - 26'''

# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

rainfall = []

for month in range(1, 13):
    month_rainfall = float(input(f'Enter rainfall for month {month}: '))
    rainfall.append(month_rainfall)

total_rainfall = sum(rainfall)
average_rainfall = total_rainfall / len(rainfall)

highest_rainfall = max(rainfall)
highest_month = rainfall.index(highest_rainfall)

lowest_rainfall = min(rainfall)
lowest_month = rainfall.index(lowest_rainfall)

print(f'Total rainfall: {total_rainfall:.2f}')
print(f'Average rainfall: {average_rainfall:.2f}')
print(f'Highest rainfall: {highest_rainfall:.2f}; Occurred in month {highest_month}')
print(f'Lowest rainfall: {lowest_rainfall:.2f}; Occurred in month {lowest_month}')