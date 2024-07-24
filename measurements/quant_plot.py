import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Step 1: Open the text file and read the data
x_data = []
y_data = []
z_data = []  # For storing z-axis data
value_data = []  # For storing 'value' which could be used for color or size
resolution_data = []  # Assuming you might use 'resolution' for additional analysis or plotting
range_data = []

with open('data.txt', 'r') as file:
    for line in file:
        # Step 3: Split the line by semicolon
        x, y, z, value, resolution, range = line.strip().split(';')
        # Step 3b: Convert string to float or int as needed
        x_data.append(float(x))
        y_data.append(float(y))
        z_data.append(float(z))
        value_data.append(float(value))
        resolution_data.append(float(resolution))  # Assuming resolution is categorical or descriptive
        range_data.append(float(range))

value_data.sort(reverse = True) #25.75;26.5;0
print(value_data)