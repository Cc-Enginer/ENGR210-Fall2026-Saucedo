#HW07 Problem #5
import numpy as np

# Unknowns: Ax, Ay, Ey, AD, AB, BC, BD, CD, CE, DE

A = np.array([

    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],

    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 1, 3/5, 0, 0, 0],

    [0, 0, 0, 0, -1, 0, -4/5, 0, 0, 0],

    [0, 0, 0, 0, 0, -1, 0, 0, 3/5, 0],

    [0, 0, 0, 0, 0, 0, 0, -1, -4/5, 0],

    [0, 0, 0, -1, 0, 0, -3/5, 0, 0, 1],

    [0, 0, 0, 0, 0, 0, 4/5, 1, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, -3/5, -1],

    [0, 0, 1, 0, 0, 0, 0, 0, 4/5, 0]

], dtype=float)

b = np.array([

    0, 0, -74, 0, 0, 24, 0, 0, 0, 0

], dtype=float)

# Solve the equations

x = np.linalg.solve(A, b)

# Print each answer separately

print("Ax =", round(x[0], 3), "kN")

print("Ay =", round(x[1], 3), "kN")

print("Ey =", round(x[2], 3), "kN")

print("AD =", round(x[3], 3), "kN")

print("AB =", round(x[4], 3), "kN")

print("BC =", round(x[5], 3), "kN")

print("BD =", round(x[6], 3), "kN")

print("CD =", round(x[7], 3), "kN")

print("CE =", round(x[8], 3), "kN")

print("DE =", round(x[9], 3), "kN")


