import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

x_data = []
y_data = []
z_data = []  
value_data = []  
resolution_data = []  
range_data = []

data = pd.read_csv('measurements/data_0.txt', sep=';', header=None)

x = data[0].values
y = data[1].values
z = data[2].values
value_data = data[3].values

norm = Normalize(vmin=value_data.min(), vmax=value_data.max())
cmap = plt.cm.viridis  

sm = ScalarMappable(norm=norm, cmap=cmap)

sizes = value_data * 10000  

fig, ax = plt.subplots()

scatter = ax.scatter(x, y, c=value_data, s=sizes, cmap=cmap, norm=norm, edgecolor='face')

ax.plot(25.75, 26.5, 'rx', markersize=4, markeredgewidth=2) #finding the center of the source by looking for the highest value of Gy (-> sorting_plot.py)
ax.plot(25.65, 26.4, 'bx', markersize=4, markeredgewidth=2) #our center

cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Dose [Gy]')

ax.set_xlabel('X coordinate [mm]')
ax.set_ylabel('Y coordinate [mm]')

plt.show()