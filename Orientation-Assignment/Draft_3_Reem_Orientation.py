import numpy as np
from matplotlib import pyplot as plt
import time

z = np.zeros(5)
b = len(z)

Npart = np.zeros(b)
### JJF Comment: DOn't declare your m, v, q, x, T arrays here
m = np.zeros(b)
v = np.zeros(b)
q = np.zeros(b)
x = np.zeros(b)
T = np.zeros(b)

for i in range(0, b):
    Npart[i] = 10*(i+1)
    
start_T = time.time()

### JJF Comment:  This loop still will only 
### compute the kinetic energy for a system of 5 particles... 
### len(Npart) = 5.  You want to use the elements of the Npart array 
### to set the length of your m, q, x, v, and T arrays...
for i in range(0, len(Npart)):
    ### JJF Comment: declare your m, q, x, v, T arrays here e.g.
    ### m = np.zeros(Npart[i]) then have one more loop nested within this loop
    ### to assign the values of the arrays, e.g.
    ### for j in range(0,Npart[i]):
    ###     m[j] = 1.0, etc
    m[i] = 1.0
    q[i] = 1.0
    x[i] = 0.5 * i
    v[i] = 0.2 * i
    T[i] = 0.5*m[i]*v[i]**2
    
end_T = time.time()
    
time_T = end_T-start_T
print("here", time_T)    

print(m)
print(q)
print(x)
print(v)
print(T)

x1 = Npart
y1 = T

print(x1, y1)

plt.figure(1)
plt.title('Time to Calculate T_tot vs. N')
plt.xlabel('Number of Particles')
plt.ylabel('Time (s)')
plt.plot(x1, y1, 'orange')
