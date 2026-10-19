A = [[4.0, -1.0, 1.0],
     [2.0, 5.0, 2.0],
     [1.0, 2.0, 4.0]]
b = [8.0, 3.0,11.0]

n = len(b)

for k in range(n-1):
    for i in range(k+1, n):
        factor = A[i][k]/A[k][k]
        for j in range(0,n):
            A[i][j] = A[i][j] - factor * A[k][j]
        b[i] = b[i] - factor*b[k]
        
        
print(A)
#back substitution
b[n-1] = b[n-1]/ A[n-1][n-1]
for i in range(n-2, -1, -1):
    sumation = b[i]
    for j in range(i+1, n):
        sumation = sumation - b[j]*A[i][j]
    b[i] = sumation/A[i][i]
print(b)
