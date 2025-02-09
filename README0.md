![image](https://github.com/user-attachments/assets/a98e7b10-3ab4-42ba-9636-d985833afa0d)


``` Python Jupyter

import matplotlib.pyplot as plt
import numpy as np

# Define the parametric equations for the trajectories
def r1(t):
    return np.array([1 + 2*t, 3 - t, -2 + t])

def r2(s):
    return np.array([3 + 0*s, -1 + (1/np.sqrt(2))*s, 4 + (1/np.sqrt(2))*s])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate values for t and s
t_values = np.linspace(-5, 5, 100)
s_values = np.linspace(-5, 5, 100)

# Plot the first trajectory r1(t)
r1_points = np.array([r1(t) for t in t_values])
ax.plot(r1_points[:, 0], r1_points[:, 1], r1_points[:, 2], label='r1(t) = <1 + 2t, 3 - t, -2 + t>', color='blue')

# Plot the second trajectory r2(s)
r2_points = np.array([r2(s) for s in s_values])
ax.plot(r2_points[:, 0], r2_points[:, 1], r2_points[:, 2], label='r2(s) = <3, -1 + s/√2, 4 + s/√2>', color='red')

# Mark the initial points
ax.scatter([1], [3], [-2], color='blue', s=100, label='Initial point of r1(t): (1, 3, -2)')
ax.scatter([3], [-1], [4], color='red', s=100, label='Initial point of r2(s): (3, -1, 4)')

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add annotations for direction vectors
ax.quiver(1, 3, -2, 2, -1, 1, color='blue', label='Direction vector of r1(t): <2, -1, 1>')
ax.quiver(3, -1, 4, 0, 1/np.sqrt(2), 1/np.sqrt(2), color='red', label='Direction vector of r2(s): <0, 1/√2, 1/√2>')

# Set the legend
ax.legend()

# Show the plot
plt.show()

```
