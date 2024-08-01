import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

file_path = 'measurements/data_4.txt'
data = pd.read_csv(file_path, delimiter=';', header=None)

x = data[0].values
y = data[1].values
z = data[2].values
data_values = data[3].values

r_0 = np.array([25.55, 26.3, 0])

R = np.sqrt(r_0[0]**2 + r_0[1]**2 + r_0[2]**2) + np.sqrt((x - r_0[0])**2 + (y - r_0[1])**2 + (z - r_0[2])**2)

def gaussian(r, A, mu, sigma):
    return A * np.exp(-(r - mu)**2 / (2 * sigma**2))

initial_guess = [np.max(data_values), np.mean(R), np.std(R)]

gaussian_params, gaussian_covariance = curve_fit(gaussian, R, data_values, p0=initial_guess)
A, mu, sigma = gaussian_params
gaussian_fitted_values = gaussian(R, A, mu, sigma)

print('A:\n', A)
print('mu:\n', mu)
print('sigma:\n', sigma)

plt.figure(figsize=(10, 6))
plt.plot(R, data_values, 'k.', label='Original Data')
plt.plot(R, gaussian_fitted_values, 'b--', label=f'Gaussian Fit: $A \\cdot e^{{-(R - {mu:.2f})^2 / (2 \\cdot {sigma:.2f}^2)}}$')
plt.xlabel('Distance from r_0 [mm]')
plt.ylabel('Data Values [Gy]')
plt.legend()
plt.grid(True)
plt.show()
