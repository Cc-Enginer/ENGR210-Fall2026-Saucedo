#HW07 Problem 1
import numpy as np
A = [[4, -1, 1],
     [2,5,2],
     [1,2,4]]
b = [8,3,11]
soln = np.linalg.solve(A,b)
print(soln)


#
check = np.dot(A,soln)
print(check)
