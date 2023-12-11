import numpy as np
import matplotlib.pyplot as plt

# Constants
wavelength = 500e-9  # meters
slit_distance = 0.5e-3  # meters
slit_width = 100e-6  # meters
screen_distance = 1  # meters
screen_width = 10e-2  # meters
N = 1000  # number of points to plot

# Derived values
k = 2 * np.pi / wavelength
beta = k * slit_distance
alpha = k * slit_width / 2

# Create x-axis
x = np.linspace(-screen_width / 2, screen_width / 2, N)

# Calculate intensity
I = (np.sinc(beta * x / screen_distance) ** 2) * (np.sin(alpha * x / screen_distance) ** 2)

# Plot intensity
plt.plot(x, I)
plt.xlabel('Position on screen (m)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Intensity pattern of Young\'s double slit experiment')
plt.show()