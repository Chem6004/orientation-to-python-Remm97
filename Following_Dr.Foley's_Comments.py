import numpy as np
from matplotlib import pyplot as plt
import time

z = np.zeros(5)
b = len(z)

Npart = np.zeros(b)

for i in range(0, b):
    Npart[i] = 10*(i+1)
    
start_T = time.time()
print(start_T)

for i in range(0, len(Npart)):
    m = np.zeros(b)
    v = np.zeros(b)
    q = np.zeros(b)
    x = np.zeros(b)
    T = np.zeros(b)
    
    for j in range(0, len(Npart)):
        m[i] = 1.0
        q[i] = 1.0
        x[i] = 0.5
        v[i] = 0.2 * i
        T[i] = 0.5*m[i]*v[i]**2
    
end_T = time.time()
print(end_T)
        
time_T = end_T-start_T
print("here", time_T)   

#print(m)
#print(q)
#print(x)
#print(v)
#print(T)

x1 = Npart
y1 = T

print(x1, y1)

plt.figure(1)
plt.title('Kinetic Energy (T) vs. N')
plt.xlabel('Number of Particles')
plt.ylabel('Total Kinetic Energy (T)')
plt.plot(x1, y1, 'orange')