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

file_path = 'measurements/data_4.txt'

with open(file_path, 'r') as file:
    for line in file:
        x, y, z, value, resolution, range = line.strip().split(';')
        x_data.append(float(x))
        y_data.append(float(y))
        z_data.append(float(z))
        value_data.append(float(value))
        resolution_data.append(float(resolution))  
        range_data.append(float(range))
    
vmin = min(value_data)
vmax = max(value_data)
norm = Normalize(vmin=vmin, vmax=vmax)
cmap = plt.cm.viridis  

sm = ScalarMappable(norm=norm, cmap=cmap)

    
sizes = np.array(value_data) * 400000  
fig, ax = plt.subplots()

scatter = ax.scatter(x_data, y_data, c=value_data, s=sizes, cmap=cmap, norm=norm)
ax.plot(25.55, 26.3, 'rx', markersize=4, markeredgewidth=2) #finding the center of the source by looking for the highest value of Gy (-> sorting_4mm.py)
ax.plot(25.65, 26.4, 'bx', markersize=4, markeredgewidth=2) #our center
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Dose [Gy]')


ax.set_xlabel('X coordinate [mm]')
ax.set_ylabel('Y coordinate [mm]')

plt.show()
