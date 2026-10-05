#HW04 prob 2
import numpy as np

import matplotlib.pyplot as plt

def trapezoidal_rule(f, x0, xN, N):

    """

    Numerically integrates f(x) from x0 to xN

    using the trapezoidal rule with N trapezoids.

    """

    h = (xN - x0) / N

    x = np.linspace(x0, xN, N + 1)

    y = f(x)

    integral = h * (y[0] / 2 + np.sum(y[1:-1]) + y[-1] / 2)

    return integral

def sine_function(x):

    return np.sin(x)

def cosine_function(x):

    return np.cos(x)

if __name__ == "__main__":

    # ------------------------------------------------

    # Verification 1: Integral of sin(x)

    # ------------------------------------------------

    # Integral of sin(x) from 0 to pi is 2

    N_values = [4, 8, 16, 32, 64, 128]

    sine_errors = []

    for N in N_values:

        result = trapezoidal_rule(sine_function, 0, np.pi, N)

        error = abs(result - 2.0)

        sine_errors.append(error)

    print("Sine function:")

    for N, error in zip(N_values, sine_errors):

        print("N =", N, "Error =", error)

    # ------------------------------------------------

    # Verification 2: Integral of cos(x)

    # ------------------------------------------------

    # Integral of cos(x) from 0 to pi/2 is 1

    cosine_errors = []

    for N in N_values:

        result = trapezoidal_rule(

            cosine_function, 0, np.pi / 2, N

        )

        error = abs(result - 1.0)

        cosine_errors.append(error)

    print("\nCosine function:")

    for N, error in zip(N_values, cosine_errors):

        print("N =", N, "Error =", error)

    # ------------------------------------------------

    # Plot 1: Integral of sin(x) as upper limit x

    # ------------------------------------------------

    x_values = np.linspace(0, np.pi, 100)

    integral_values = []

    for x in x_values:

        integral = trapezoidal_rule(sine_function, 0, x, 100)

        integral_values.append(integral)

    plt.figure()

    plt.plot(x_values, integral_values)

    plt.xlabel("Upper limit x")

    plt.ylabel("Integral of sin(x)")

    plt.title("Integral of sin(x) from 0 to x")

    plt.grid()

    plt.show()

    # ------------------------------------------------

    # Plot 2: Truncation error for sin(x)

    # ------------------------------------------------

    plt.figure()

    plt.loglog(N_values, sine_errors, 'o-')

    plt.xlabel("Number of trapezoids N")

    plt.ylabel("Error")

    plt.title("Trapezoidal Rule Error for sin(x)")

    plt.grid()

    plt.show()

    # ------------------------------------------------

    # Plot 3: Truncation error for cos(x)

    # ------------------------------------------------

    plt.figure()

    plt.loglog(N_values, cosine_errors, 'o-')

    plt.xlabel("Number of trapezoids N")

    plt.ylabel("Error")

    plt.title("Trapezoidal Rule Error for cos(x)")





plt.grid()
plt.show()



