import numpy as np

import matplotlib.pyplot as plt

# Given parameters

L = 10.0

h = 0.01

Ta = 20.0

T0 = 200.0

h_tip = 0.001

grid_sizes = [1.0, 0.1, 0.01]

# Analytical solution for Problem 2

def exact2(x):

    k = np.sqrt(h)

    return Ta + (T0 - Ta) * np.cosh(k * (L - x)) / np.cosh(k * L)

# Analytical solution for Problem 3

def exact3(x):

    k = np.sqrt(h)

    r = h_tip / k

    top = np.cosh(k * (L - x)) + r * np.sinh(k * (L - x))

    bottom = np.cosh(k * L) + r * np.sinh(k * L)

    return Ta + (T0 - Ta) * top / bottom

# Finite difference solver

def solve(dx, problem):

    n = int(round(L / dx))

    dx = L / n

    # Unknown temperatures: T1 through Tn

    A = np.zeros((n, n))

    b = np.zeros(n)

    # Interior nodes

    for j in range(1, n):

        row = j - 1

        A[row, row] = 2.0 + h * dx**2

        A[row, row + 1] = -1.0

        b[row] = h * dx**2 * Ta

        if j == 1:

            b[row] += T0

        else:

            A[row, row - 1] = -1.0

    # Right boundary: insulated or heat-losing tip

    A[n - 1, n - 2] = -2.0

    if problem == 2:

        # Insulated tip: dT/dx = 0

        A[n - 1, n - 1] = 2.0 + h * dx**2

        b[n - 1] = h * dx**2 * Ta

    else:

        # Heat loss at tip

        A[n - 1, n - 1] = 2.0 + h * dx**2 + 2.0 * dx * h_tip

        b[n - 1] = (h * dx**2 + 2.0 * dx * h_tip) * Ta

    # Solve linear equations

    interior = np.linalg.solve(A, b)

    # Add left boundary temperature

    T = np.zeros(n + 1)

    T[0] = T0

    T[1:] = interior

    x = np.linspace(0.0, L, n + 1)

    return x, T

# Run both problems

for problem in [2, 3]:

    if problem == 2:

        exact = exact2

        title = "Problem 2: Insulated Tip"

    else:

        exact = exact3

        title = "Problem 3: Heat Loss at Tip"

    errors = []

    print()

    print(title)

    print("------------------------------")

    # Temperature plot

    plt.figure(figsize=(8, 5))

    for dx in grid_sizes:

        x, T = solve(dx, problem)

        T_exact = exact(x)

        error = np.max(np.abs(T - T_exact))

        errors.append(error)

        print("Grid size:", dx, "m")

        print("Tip temperature:", round(T[-1], 6), "C")

        print("Maximum error:", "{:.8e}".format(error))

        print()

        plt.plot(x, T, label="dx = " + str(dx) + " m")

    # Analytical curve

    x_fine = np.linspace(0.0, L, 1001)

    plt.plot(x_fine, exact(x_fine), "k--",

             label="Analytical solution")

    plt.xlabel("Distance (m)")

    plt.ylabel("Temperature (C)")

    plt.title(title)

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()

    # Calculate convergence rates

    print("Convergence rates:")

    for i in range(len(grid_sizes) - 1):

        rate = np.log(errors[i] / errors[i + 1]) / np.log(

            grid_sizes[i] / grid_sizes[i + 1]

        )

        print(

            str(grid_sizes[i]) + " to "

            + str(grid_sizes[i + 1]) + " m:",

            round(rate, 4)

        )

    # Error convergence plot

    reference_errors = []

    for dx in grid_sizes:

        reference_errors.append(

            errors[0] * (dx / grid_sizes[0])**2

        )

    plt.figure(figsize=(7, 5))

    plt.loglog(grid_sizes, errors, "o-",

               label="Numerical error")

    plt.loglog(grid_sizes, reference_errors, "--",

               label="Second-order reference")

    plt.xlabel("Grid size (m)")

    plt.ylabel("Maximum absolute error")

    plt.title("Convergence for Problem " + str(problem))

    plt.grid(True, which="both")

    plt.legend()

    plt.tight_layout()

    plt.show()

print()

print("Both problems completed.")
