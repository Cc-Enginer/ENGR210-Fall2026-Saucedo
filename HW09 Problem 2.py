
import numpy as np

L = 0.01
k = 10
hL = 100
hR = 50

TL = 500
TR = 300

n = 20
dx = L/n

# Analytical solution
q_exact = (TL-TR)/(1/hL + L/k + 1/hR)

x = (np.arange(n)+0.5)*dx

T_exact = TL - q_exact*(1/hL + x/k)

# Gauss-Seidel solution
G = k/dx
GL = 1/(dx/(2*k)+1/hL)
GR = 1/(dx/(2*k)+1/hR)

T = np.ones(n)*400

for iteration in range(100000):

    error = 0

    for i in range(n):

        old = T[i]

        if i == 0:
            T[i] = (GL*TL + G*T[i+1])/(GL+G)

        elif i == n-1:
            T[i] = (G*T[i-1] + GR*TR)/(G+GR)

        else:
            T[i] = (G*T[i-1]+G*T[i+1])/(2*G)

        error = max(error, abs(T[i]-old))

    if error < 1e-10:
        break

print("Analytical heat flux:", q_exact)
print("Numerical temperatures:")
print(T)

print("Analytical temperatures:")
print(T_exact)

print("Maximum temperature error:",
      np.max(np.abs(T-T_exact)))
