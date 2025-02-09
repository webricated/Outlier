import numpy as np
import matplotlib.pyplot as plt

# Define the given angles (in radians)
angles = np.array([np.pi/7, 2*np.pi/7, 3*np.pi/7])

# Compute tan²(θ) and cot²(θ)
tan_squared = np.tan(angles) ** 2
cot_squared = 1 / tan_squared  # cotangent squared is the reciprocal of tangent squared

# --- POLAR PLOT (Unit Circle Representation) ---
fig, ax = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'projection': [None, 'polar'][0]})

ax[0] = plt.subplot(121, projection='polar')  # Left plot is a polar plot

ax[0].set_title("Polar Representation of tan²(θ) & cot²(θ)", fontsize=12)

# Plot tan²(θ) values as outward radial lines
ax[0].plot(angles, tan_squared, 'bo', label=r'$\tan^2(\theta)$')

# Plot cot²(θ) values as inward radial lines
ax[0].plot(angles, cot_squared, 'ro', label=r'$\cot^2(\theta)$')

ax[0].set_xticks(angles)  # Set angle labels
ax[0].legend()

# --- BAR CHART (Comparison of Values) ---
ax[1] = plt.subplot(122)  # Right plot is a bar chart
width = 0.3  # Bar width
indices = np.arange(len(angles))

ax[1].bar(indices - width/2, tan_squared, width, label=r'$\tan^2(\theta)$', color='b')
ax[1].bar(indices + width/2, cot_squared, width, label=r'$\cot^2(\theta)$', color='r')

ax[1].set_xticks(indices)
ax[1].set_xticklabels([r'$\frac{\pi}{7}$', r'$\frac{2\pi}{7}$', r'$\frac{3\pi}{7}$'])
ax[1].set_title("Bar Chart Comparison")
ax[1].set_ylabel("Function Values")
ax[1].legend()

# Show the plot
plt.tight_layout()
plt.show()
