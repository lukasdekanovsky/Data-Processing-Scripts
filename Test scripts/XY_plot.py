import matplotlib.pyplot as plt

# Open the .txt file
with open('./data/test.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()

# Initialize empty lists for x and y values
x_values = []
y_values = []

# Parse the data from each line and append to the respective lists
for line in lines:
    data = line.split()
    try:
        x_values.append(float(data[0]))
        y_values.append(float(data[1]))
    except ValueError:
        continue

# Plot the data
plt.plot(x_values, y_values)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of Data')
plt.show()