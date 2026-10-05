import numpy as np

def trapezoidal_rule(x, y):

    total = 0

    for i in range(len(x) - 1):

        total += ((y[i] + y[i + 1]) / 2) * (x[i + 1] - x[i])

    return total

if __name__ == "__main__":

    # Stress-strain data from the experiment

    stress = np.array([40, 37.5, 43, 52, 60, 55])

    strain = np.array([0.02, 0.05, 0.10, 0.15, 0.20, 0.25])

    # Calculate modulus of toughness

    toughness = trapezoidal_rule(strain, stress)

    print("Modulus of toughness =", toughness, "ksi")

