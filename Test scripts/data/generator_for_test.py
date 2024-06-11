import math

# Define the number of values in each column
num_values = 100

# Open the file for writing
with open('./data/test.txt', 'w') as file:
    # Write the column headers
    file.write('Column 1\tColumn 2\n')

    # Generate and write the data
    for i in range(num_values):
        x = i + 1
        y = math.exp(x)
        file.write(f'{x}\t{y}\n')