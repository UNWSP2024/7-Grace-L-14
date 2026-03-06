'''Population Program
By Grace LeVoir
3 - 5 - 26'''

# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    # Now have the user enter a year. 
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

all_entered_values = []

rows = int(input('Enter the number of data sets: '))

for data_set in range(rows):
    year = int(input(f'Enter the year for data set {data_set+1}: '))
    state = input(f'Enter the state for data set {data_set+1}: ')
    population = int(input(f'Enter the population for data set {data_set+1}: '))

    data = [year,state,population]
    all_entered_values.append(data)

year_to_sum = int(input('Enter the year to sum: '))


def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user entered 2010 for the year to sum,
    # or 3,421,988 if they entered 2011 for the year to sum.

    total = 0
    for row in all_entered_values:
        if row[0] == year_to_sum:
            total += row[2]

    return total



    # print the totalled population

total_population = sum_population_for_year(all_entered_values, year_to_sum)

print(total_population)

# Call the main function.
if __name__ == '__main__':
    main()