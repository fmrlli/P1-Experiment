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

# Normalize the 'value' for color mapping
norm = Normalize(vmin=min(value_data), vmax=max(value_data))
cmap = plt.cm.viridis  # Choose a colormap; you can use 'viridis', 'plasma', 'inferno', etc.

# Create a ScalarMappable object to use the colormap and normalization
sm = ScalarMappable(norm=norm, cmap=cmap)

# Scale 'value' for size mapping (optional scaling factor)
sizes = np.array(value_data) * 10000  # Adjust this factor as needed for better visual distinction

# Plot the scatter plot
fig, ax = plt.subplots()

scatter = ax.scatter(x_data[0:671], y_data[0:671], c=value_data[0:671], s=sizes[0:671], cmap=cmap, norm=norm)

# Adding colorbar to show the color gradient mapping
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Value')

ax.set_xlabel('X Axis Label')
ax.set_ylabel('Y Axis Label')

plt.show()
