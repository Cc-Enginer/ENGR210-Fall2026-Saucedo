
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------
# 1. Define the grid
# --------------------------------

Lx = 1.0
Ly = 1.0

nx = 21
ny = 21

dx = Lx / (nx - 1)
dy = Ly / (ny - 1)

# Temperature matrix
T = np.zeros((ny, nx))

# --------------------------------
# 2. Apply boundary conditions
# --------------------------------

# Bottom = 0 degrees C
T[0, :] = 0

# Top = 100 degrees C
T[-1, :] = 100

# Left = 75 degrees C
T[:, 0] = 75

# Right = 50 degrees C
T[:, -1] = 50

# Set corner temperatures to averages
T[0, 0] = (0 + 75) / 2
T[0, -1] = (0 + 50) / 2
T[-1, 0] = (100 + 75) / 2
T[-1, -1] = (100 + 50) / 2

# --------------------------------
# 3. Gauss-Seidel settings
# --------------------------------

tolerance = 1e-6
max_iterations = 100000

error = 1.0
iteration = 0

# --------------------------------
# 4. Gauss-Seidel iteration
# --------------------------------

while error > tolerance and iteration < max_iterations:

    error = 0.0

    for j in range(1, ny - 1):
        for i in range(1, nx - 1):

            old_temperature = T[j, i]

            new_temperature = 0.25 * (
                T[j, i + 1] +
                T[j, i - 1] +
                T[j + 1, i] +
                T[j - 1, i]
            )

            T[j, i] = new_temperature

            change = abs(new_temperature - old_temperature)

            if change > error:
                error = change

    iteration += 1

# --------------------------------
# 5. Display results
# --------------------------------

print("Gauss-Seidel Solution")
print("---------------------")
print("Iterations:", iteration)
print("Final error:", error)

print("Temperature Matrix:")
print(np.round(T, 2))

print("Maximum temperature:", np.max(T), "C")
print("Minimum temperature:", np.min(T), "C")

# --------------------------------
# 6. Create coordinate grid
# --------------------------------

x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)

X, Y = np.meshgrid(x, y)

# --------------------------------
# 7. Plot using imshow
# --------------------------------

plt.figure()

plt.imshow(
    T,
    extent=[0, Lx, 0, Ly],
    origin='lower',
    cmap='hot',
    aspect='equal'
)

plt.colorbar(label='Temperature (C)')
plt.xlabel('Distance x (m)')
plt.ylabel('Distance y (m)')
plt.title('Temperature Distribution - imshow')

plt.show()

# --------------------------------
# 8. Plot using contour
# --------------------------------

plt.figure()

contours = plt.contour(
    X, Y, T,
    levels=15,
    cmap='hot'
)

plt.clabel(contours, inline=True, fontsize=8)

plt.colorbar(label='Temperature (C)')
plt.xlabel('Distance x (m)')
plt.ylabel('Distance y (m)')
plt.title('Temperature Distribution - Contour')

plt.show()
