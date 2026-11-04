import numpy as np

import matplotlib.pyplot as plt

# Given information

L = 10.0

dx = 0.10

hp = 0.02

Ta = 10.0

T_right = 200.0

# Number of grid intervals and points

n = int(L / dx)

x = np.linspace(0, L, n + 1)

# Calculate h' * dx^2

a = hp * dx**2

# Create coefficient matrix and right-hand side

A = np.zeros((n, n))

b = np.ones(n) * a * Ta

# Insulated left boundary

A[0, 0] = 2 + a

A[0, 1] = -2

# Interior points

for i in range(1, n):

    A[i, i] = 2 + a

    A[i, i-1] = -1

    if i < n - 1:

        A[i, i+1] = -1

# Fixed temperature at the right boundary

b[-1] = b[-1] + T_right

# Solve the system of equations

T_unknown = np.linalg.solve(A, b)

# Add the right boundary temperature

T = np.append(T_unknown, T_right)

# Display temperatures

print("Distance (m)     Temperature (C)")

for i in range(0, n + 1, 10):

    print(f"{x[i]:8.2f}          {T[i]:8.2f}")

# Plot temperature distribution

plt.plot(x, T, 'b-', label='Temperature')

plt.xlabel('Distance (m)')

plt.ylabel('Temperature (C)')

plt.title('Temperature Distribution Along Insulated Rod')

plt.grid(True)
plt.legend()
plt.show()