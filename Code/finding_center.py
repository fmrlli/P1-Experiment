import numpy as np

data = np.loadtxt('measurements/data_0.txt', delimiter=';')


x_values = data[:, 0]
y_values = data[:, 1]

center_x = np.mean(x_values)
center_y = np.mean(y_values)

print(center_x, center_y)
