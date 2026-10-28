import numpy as np
import matplotlib.pyplot as plt
# Coefficients
hpr = .01
L = 10
Tleft, Tright, tambient = 200, 40, 20
n = 11 # number of grid points
dx = L/(n-1)  #spacing in m
# Create A and b
A = np.zeros((n,n), dtype=float) # 2D array with shape n by n where n is the # of points# this is coefficients
b = np.zeros(n, dtype=float) # 1D vector with shape n # This is the constants
# Fill in A and b
np.fill_diagonal(A[1:-1,1:-1],  -(2+hpr*dx**2))
np.fill_diagonal(A[1:-1,0:-2], 1)
np.fill_diagonal(A[1:-1,2:], 1)
A[0,0], A[-1,-1] = 1,1 #Fixed temperature boundary conditions
b[1:-1] = -hpr*tambient
b[0], b[-1] = 200, 40 #Fixed Temperature BCs
print(b)
# Run linalg.solve to find T
T = np.linalg.solve(A, b)

#Plot T vs x
x_arr = np.linspace(0,L,n)
plt.figure(figsize=(5,5))
plt.plot(x_arr, T)
plt.show()
