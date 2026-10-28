import numpy as np


import matplotlib.pyplot as plt

# Given values

L = 10.0

h = 0.01

Ta = 20.0

T0 = 200.0

TL = 40.0

# Analytical solution

def exact_temperature(x):

    k = np.sqrt(h)

    return (Ta

            + (T0 - Ta) * np.sinh(k * (L - x))

            / np.sinh(k * L)

            + (TL - Ta) * np.sinh(k * x)

            / np.sinh(k * L))

# Finite difference solution

def solve_temperature(dx):

    n = int(round(L / dx))

    x = np.linspace(0, L, n + 1)

    # Number of interior points

    m = n - 1

    # Create coefficient matrix and right-hand side

    A = np.zeros((m, m))

    b = np.zeros(m)

    for i in range(m):

        A[i, i] = 2 + h * dx**2

        b[i] = h * dx**2 * Ta

        if i > 0:

            A[i, i - 1] = -1

        if i < m - 1:

            A[i, i + 1] = -1

    # Apply boundary temperatures

    b[0] = b[0] + T0

    b[m - 1] = b[m - 1] + TL

    # Solve the system

    interior = np.linalg.solve(A, b)

    # Add the two boundary temperatures

    T = np.zeros(n + 1)

    T[0] = T0

    T[-1] = TL

    T[1:-1] = interior

    return x, T

# Grid sizes

steps = [1.0, 0.1, 0.01]

errors = []

# Plot temperature distributions

plt.figure(figsize=(9, 6))

for dx in steps:

    x, T = solve_temperature(dx)

    T_exact = exact_temperature(x)

    error = np.max(np.abs(T - T_exact))

    errors.append(error)

    print("Grid size:", dx, "m")

    print("Maximum error:", "{:.8e}".format(error), "degrees C")

    print()

    plt.plot(x, T, label="dx = " + str(dx) + " m")

# Plot exact solution

x_exact = np.linspace(0, L, 1001)

plt.plot(x_exact, exact_temperature(x_exact),

         "k--", label="Analytical solution")

plt.xlabel("Distance (m)")

plt.ylabel("Temperature (degrees C)")

plt.title("Temperature Along the Rod")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()

# Calculate convergence rates

print("CONVERGENCE RATES")

for i in range(len(steps) - 1):

    p = np.log(errors[i] / errors[i + 1]) / np.log(

        steps[i] / steps[i + 1]

    )

    print("From dx =", steps[i], "to dx =", steps[i + 1])

    print("Convergence rate =", round(p, 4))

    print()

# Plot error versus grid size

plt.figure(figsize=(7, 5))

plt.loglog(steps, errors, "o-", label="Numerical error")

plt.loglog(

    steps,

    [errors[0] * (dx / steps[0])**2 for dx in steps],

    "--",

    label="Second-order reference"

)

plt.xlabel("Grid size (m)")

plt.ylabel("Maximum absolute error")

plt.title("Convergence Check")

plt.legend()

plt.grid(True, which="both")

plt.tight_layout()

plt.show()