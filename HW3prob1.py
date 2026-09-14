import numpy as np
import matplotlib.pyplot as plt
  
  
A = 2
T =24

t = np.linspace(0, 2 * T, 500)


sine = A * np.sin(2 * np.pi * t / T)
cosine = A * np.cos(2 * np.pi * t / T)

plt.plot (t, sine, color = "green", linestyle = "--", label="sine")
plt.plot (t, cosine, color = "red", linestyle = "-.", label="cosine")
plt.xlabel("x")
plt.ylabel("f(t)")
plt.legend()
plt.show()