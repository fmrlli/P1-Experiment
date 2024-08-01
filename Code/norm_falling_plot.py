import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'measurements/data_0.txt'

data = pd.read_csv(file_path, delimiter=';', header=None)

x = data[0].values
y = data[1].values
z = data[2].values
data_values = data[3].values
norm_data = data_values / 0.02507

r = np.sqrt(x**2 + y**2 + z**2)

r_0 = np.array([25.75, 26.5, 0])

R = np.sqrt((x - r_0[0])**2 + (y - r_0[1])**2 + (z - r_0[2])**2)

plt.figure(figsize=(10, 6))
plt.plot(R, norm_data, 'k.')
plt.xlabel('Distance from r_0 [mm]')
plt.ylabel('Data Values [Gy]')
plt.grid(True)
plt.show()
