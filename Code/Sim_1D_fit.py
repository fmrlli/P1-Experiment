import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

with open('simulation/praktikum001_fort.21 - Copy.txt', 'r') as file:
    data = file.read().split()

values = [float(x) * 1000 for x in data]

values = values[218:]

space = np.arange(0, 9, 0.0115)

space = space[:len(values)]

def inverse_square(r, a, b):
    return a / (r - b)**2

popt, _ = curve_fit(inverse_square, space, values, p0=[1, -2.5])

a_fit, b_fit = popt

space_smooth = np.linspace(space.min(), space.max(), 1000)

plt.figure(figsize=(12, 6))
plt.plot(space, values, 'b.', label='Data')
plt.plot(space_smooth, inverse_square(space_smooth, *popt), 'r-', label=f'Fit: $a/(r-b)^2$, a={a_fit:.3e}, b={b_fit:.3e}')
plt.xlabel('x coordinate [mm]')
plt.ylabel('Energy [GeV]')

plt.legend()
plt.grid(True)

print(f"Fitted function: y = {popt[0]:.4f} / (r - {popt[1]:.4f})²")

plt.show()