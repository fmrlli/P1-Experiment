import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'measurements/data_longrun.txt'
data = pd.read_csv(file_path, delimiter=';', header=None)

x = data[0].values
y = data[1].values
z = data[2].values
data_values = data[3].values
error = data[4].values

adjusted_errors = []
colors = []
for err, value in zip(error, data_values):
    if err == 0:
        adjusted_errors.append(0.005 * value)  # 0.5%
        colors.append('black')
    elif err == 1:
        adjusted_errors.append(0.01 * value)   # 1%
        colors.append('red')
    elif err == 2:
        adjusted_errors.append(0.02 * value)   # 2%
        colors.append('yellow')

adjusted_errors = np.array(adjusted_errors)

plt.figure(figsize=(10, 6))
for i in range(len(z)):
    plt.errorbar(z[i], data_values[i], yerr=adjusted_errors[i], fmt='.', ecolor='gray', elinewidth=1, capsize=2, color=colors[i])

plt.xlabel('z coordinate [mm]')
plt.ylabel('Data Values [Gy]')

black_proxy = plt.Line2D([0], [0], linestyle="none", marker='o', color='black')
red_proxy = plt.Line2D([0], [0], linestyle="none", marker='o', color='red')
yellow_proxy = plt.Line2D([0], [0], linestyle="none", marker='o', color='yellow')

plt.legend([black_proxy, red_proxy, yellow_proxy], 
           ['Error = 0.5%', 'Error = 1%', 'Error = 2%'], 
           numpoints=1, loc='upper right')

plt.grid(True)

plt.show()
