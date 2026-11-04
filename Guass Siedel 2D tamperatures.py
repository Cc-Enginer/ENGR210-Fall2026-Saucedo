# intialize with the correct BC
import numpy as np
import matplotlib.pyplot as plt
Nx, Ny = 101, 101
T_arr = np.ones((Nx, Ny), dtype = float) * 50
T_arr[1:-1,0] = 0 #bottom Bc
T_arr[1:-1,-1] = 100 # Top BC
T_arr[0, 1: -1] = 75 # Left BC
T_arr[-1,1:1] = 50 # Right BC

T_arr[0,0], T_arr[-1,0], T_arr[-1,-1], T_arr[0,-1] = (0+75)/2, (0+50)/2, (50+100)/2, (100+75)/2 
tol = 1e-4 #in an absolute sense
max_err = tol + 1
#loop until error converges
while max_err > tol:
    max_err = 0
    # loop over all the grid points
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            T_new = (T_arr[i-1][j] + T_arr[i+1][j] + T_arr[1][j-1] + T_arr[1][j+1])/4
            T_new = 1.9* T_new + (1-1.9)*T_arr[i][j]
            max_err = max(max_err, abs(T_new-T_arr[i][j]))   #keeps the biggets error
            T_arr[i,j] = T_new
            
        if max_err < tol:
            print("Converged")
            break
        
plt.imshow(T_arr.T, origin = 'lower')
plt.show()
        