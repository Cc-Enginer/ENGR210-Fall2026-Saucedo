import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r'C:\Users\Cc Saucedo\OneDrive - Saint Francis University\Documents\Simple_Quad\Engr210\Isle_Royale_Moose_Wolves_data.csv',
                  delimiter=',',
                  skiprows=1)
data = np.array(data)
data[data==-9999]=np.nan
plt.figure(figsize=(5,5))
plt.plot(data[:,0], data [:,1],'o', label='Moose')
plt.plot(data[:,0], data [:,2],'s', label='Wolves')
plt.show()
plt.figure (Figsize=(5,5))
plt.plot(data[:,2], data[:,1], 'o')
plt.show()

# 
# with open("Isle_Moose", 'r') as file
#     f=file.read()
#     
# np.loadtxt(