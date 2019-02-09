import numpy as np
from matplotlib import pyplot as plt
import time

#z = np.zeros(5)
#b = len(z)

Npart = np.zeros(5)

for i in range(0, len(Npart)):
    Npart[i] = 10*(i+1)

start_T = time.time()
print(start_T)

for i in range(0, int(Npart[i])):
    m = np.zeros( int(Npart[i]) )
    v = np.zeros( int(Npart[i]) )
    q = np.zeros( int(Npart[i]) )
    x = np.zeros( int(Npart[i]) )
    T = np.zeros( int(Npart[i]) )
    
    for j in range(0, int(Npart[i])):
        m[j] = 1.0
        q[j] = 1.0
        x[j] = 0.5
        v[j] = 0.2 * i
        T[j] = 0.5*m[i]*v[i]**2
    
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