import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import Normalize

file_path = 'simulation/praktikum001_fort.22 - Copy.txt'

x_size = 1000
y_size = 110
z_size = 110

with open(file_path, 'r') as file:
    data = file.read()

data_values = data.split()

data_values = [float(value) for value in data_values]

data_array = np.array(data_values).reshape(z_size, y_size, x_size)

x_values = np.linspace(-2.5, 9, x_size)
y_values = np.linspace(-7.5, 7.5, y_size)  
z_values = np.linspace(-7.5, 7.5, z_size)  

z_grid, y_grid, x_grid = np.meshgrid(z_values, y_values, x_values, indexing='ij')

x_flat = x_grid.ravel()
y_flat = y_grid.ravel()
z_flat = z_grid.ravel()
data_flat = data_array.ravel()

# Sample 10% of the data randomly
np.random.seed(42)  # For reproducibility
sample_size = int(len(data_flat) * 0.1)  
indices = np.random.choice(len(data_flat), size=sample_size, replace=False)

x_sample = x_flat[indices]
y_sample = y_flat[indices]
z_sample = z_flat[indices]
data_sample = data_flat[indices]

transparency_threshold = 0.001

# Normalize the data values for color mapping (only for visible data)
data_sample_normalized = np.clip(data_sample, transparency_threshold, None)  
norm = Normalize(vmin=np.min(data_sample_normalized), vmax=np.max(data_sample_normalized))
colors = plt.cm.viridis(norm(data_sample_normalized))

alpha_values = np.where(data_sample < transparency_threshold, 0, 1) 
colors[:, 3] = alpha_values  


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(x_sample, y_sample, z_sample, color=colors, s=2) 
cbar = plt.colorbar(sc)
cbar.set_label('Data normalized')

ax.set_xlabel('X axis [mm]')
ax.set_ylabel('Y axis [mm]')
ax.set_zlabel('Z axis [mm]')

plt.show()
