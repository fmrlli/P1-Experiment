import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

file_path = 'measurements/data_longrun.txt'
data = pd.read_csv(file_path, delimiter=';', header=None)

x = data[0].values
y = data[1].values
z = data[2].values
data_values = data[3].values
error = data[4].values

def func(r, a, b):
    return a / (r + b)**2

popt, pcov = curve_fit(func, z, data_values)

a_fit, b_fit = popt

fitted_data = func(z, a_fit, b_fit)

plt.figure(figsize=(10, 6))
plt.plot(z, data_values, 'k.', label='Original Data')
plt.plot(z, fitted_data, 'r-', label=f'Fit: $a/(r-b)^2$, a={a_fit:.3e}, b={b_fit:.3e}')
plt.xlabel('z coordinate [mm]')
plt.ylabel('Data Values [Gy]')
plt.legend()
plt.grid(True)
plt.show()
