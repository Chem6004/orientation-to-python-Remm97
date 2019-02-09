#Reem's_Orientation_Code_Submission
#CHEM_6004_Theoretical_&_Physical_Methods
#02/08/2019

import numpy as np
from matplotlib import pyplot as plt
import time

#Kinetic_Energy:

start_KE = time.time()

z = np.zeros(6)

for i in range(1,6):
    z[i] = 5*i

#print(z)
    
b = len(z)
#print(b)
    
Npart = np.zeros(b)
m = np.zeros(b)
v = np.zeros(b)
T = np.zeros(b)
    
for i in range(0, b):
    m[i] = 1.0
    v[i] = 2.5
    Npart[i] = Npart[i] + 10*i
    T[i] = 1/2 * m[i] * v[i]**2
        
#print("Printing array of masses: ", m)
#print("Printing array of velocities", v)
#print("Printing array of Npart", Npart)
#print("Printing array of KE", T)

TvsNpart = np.zeros(b)

for i in range(0,b):
    TvsNpart[i] = T[i]*Npart[i]

x = Npart
y = TvsNpart

print("Printing array of Npart", x)
print("Printing array of KE vs N", y)

plt.figure(1)
plt.title('Energy Scaling with N')
plt.xlabel('Number of Particles')
plt.ylabel('Kinetic Energy (T)')
plt.plot(x, y, 'purple')

end_KE = time.time()

how_long_KE = np.zeros(b)

for i in range(0,b):
    how_long_KE[i] = (end_KE - start_KE)*Npart[i]
    
z = how_long_KE

print(" Total time to run KE in seconds is: ",z)

plt.figure(2)
plt.title('Time to Calculate T Scaling with N')
plt.xlabel('Number of Particles')
plt.ylabel('Time (s)')
plt.plot(x, z, 'orange')

#Potential_Energy:

start_PE = time.time()

q = np.ones(b)

x = np.linspace(0,(b-1)*0.2,b)

r = np.zeros((b,b))

for i in range(0,b):
    for j in range(0,b):
        r[i][j] = np.sqrt( (x[i]-x[j])**2 )

#print("Printing array of charges ",q)
#print("Printing array of particle positions ",x)
#print("Printing array of separation between particle pairs",r)

def Potential(sep_array, charge_array):
    N = len(charge_array)
    
    Pot = 0.

    for i in range(0,N):
        for j in range(0,N):
            if (i!=j):
               Pot = Pot + charge_array[i]*charge_array[j]/sep_array[i][j]
    
    return Pot

V_tot = np.zeros(b)

for i in range(0, b):
    Npart[i] = Npart[i] + 10*i
    V_tot[i] = Potential(r, q)
#    print(V_tot)
    
VvsNpart = np.zeros(b)

for i in range(0,b):
    VvsNpart[i] = V_tot[i]*Npart[i]
    
x1 = Npart
y1 = VvsNpart

print("Printing array of Npart", x)
print("Printing array of PE vs N", y)

plt.figure(3)
plt.title('Energy Scaling with N')
plt.xlabel('Number of Particles')
plt.ylabel('Potential Energy (V)')
plt.plot(x1, y1, 'green')

end_PE = time.time()

how_long_PE = np.zeros(b)

for i in range(0,b):
    how_long_PE [i] = (end_PE - start_PE)*Npart[i]
    
w = how_long_PE
    
print(" Total time to run PE in seconds is: ",w)

plt.figure(4)
plt.title('Time to Calculate V Scaling with N')
plt.xlabel('Number of Particles')
plt.ylabel('Time (s)')
plt.plot(x1, w, 'black')
