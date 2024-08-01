import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Read the data
data = pd.read_csv('measurements/data_0.txt', sep=';', header=None, names=['x', 'y', 'z', 'value', 'col5', 'col6'])

# Calculate the radius
data['radius'] = np.sqrt((data['x'] - data['x'].mean())**2 + (data['y'] - data['y'].mean())**2)

# Create the scatter plot
fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(data['radius'], data['value'], c=data['value'], cmap='viridis', s=20)

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Dose [Gy]')

# Set labels and title
ax.set_xlabel('Radius [mm]')
ax.set_ylabel('Dose [Gy]')
ax.set_title('Dose vs Radius')

# Add 'x' marker at the specified coordinates
center_x, center_y = data['x'].mean(), data['y'].mean()
specified_x, specified_y = 25.75, 26.5
specified_radius = np.sqrt((specified_x - center_x)**2 + (specified_y - center_y)**2)
specified_value = data[(data['x'] == specified_x) & (data['y'] == specified_y)]['value'].values
if len(specified_value) > 0:
    ax.plot(specified_radius, specified_value[0], 'rx', markersize=10, markeredgewidth=2)

plt.show()