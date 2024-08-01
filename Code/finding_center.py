import numpy as np
# Load the data from the file with the correct delimiter
data = np.loadtxt('measurements/data_0.txt', delimiter=';')

# Separate the x and y values
x_values = data[:, 0]
y_values = data[:, 1]

# Calculate the center of the 2D plane
center_x = np.mean(x_values)
center_y = np.mean(y_values)

print(center_x, center_y)
