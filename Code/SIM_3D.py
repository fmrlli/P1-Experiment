import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import Normalize

# Define the file path
file_path = 'simulation/praktikum001_fort.22 - Copy.txt'

# Define the grid sizes
x_size = 1000
y_size = 110
z_size = 110

# Read the data from the file
with open(file_path, 'r') as file:
    data = file.read()

# Split the data into individual values
data_values = data.split()

# Convert the string values to floats
data_values = [float(value) for value in data_values]

# Reshape the data according to the grid dimensions
data_array = np.array(data_values).reshape(z_size, y_size, x_size)

# Generate x, y, z coordinates
x_values = np.linspace(-2.5, 9, x_size)  # Adjusted for correct number of points
y_values = np.linspace(-7.5, 7.5, y_size)  # Adjusted for correct number of points
z_values = np.linspace(-7.5, 7.5, z_size)  # Adjusted for correct number of points

# Create a meshgrid
z_grid, y_grid, x_grid = np.meshgrid(z_values, y_values, x_values, indexing='ij')

# Flatten grids and data array
x_flat = x_grid.ravel()
y_flat = y_grid.ravel()
z_flat = z_grid.ravel()
data_flat = data_array.ravel()

# Create a DataFrame with x, y, z, and data columns
df = pd.DataFrame({
    'x': x_flat,
    'y': y_flat,
    'z': z_flat,
    'data': data_flat
})

# Filter out rows where data value is 0
df_filtered = df[df['data'] >= 0]

# Assuming you have loaded or still have the filtered DataFrame
x = df_filtered['x']
y = df_filtered['y']
z = df_filtered['z']
data = df_filtered['data']

# Create a 3D scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
sc = ax.scatter(x, y, z, c=data, cmap='cividis', s=1)  # Adjust s for point size

# Adding color bar
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Data Value [GeV]')

# Labeling axes
ax.set_xlim([-2.5, 9])
ax.set_ylim([-7.5, 7.5])
ax.set_zlim([-7.5, 7.5])
ax.set_xlabel('X axis [mm]')
ax.set_ylabel('Y axis [mm]')
ax.set_zlabel('Z axis [mm]')



plt.show()