# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:32:37 2019

@author: eldabaghr
"""

import numpy as np

#print("Hello World!")
#m = 1.0
#v = 5.0
###
#T1 = 0.5*m*v**2
#T2 = 1/2 * m * v * v
#T3 = 0.5 * m * v * v
#T4 = m*v**2/2

#print(T1, T2, T3, T4)

### variables for particle 1
#m1 = 1.0
#v1 = 5.0
#q1 = 1.0
#x1 = 0.0

### variables for particle 2
#m2 = 1.0
#v2 = 2.5
#q2 = 1.0
#x2 = 0.5

### variable for pair of particles
#r12 = np.sqrt((x1-x2)**2)
#r12moi = (((x1-x2)**2)**(1/2))

#print("Separation is", r12, r12moi)

#v12 = ((q1*q2)/(r12))

#print("Potential Energy is", v12)

### with many variables

Nparticles = 10
m = np.zeros(Nparticles)
v = np.zeros(Nparticles)
q = np.zeros(Nparticles)
x = np.zeros(Nparticles)
T = np.zeros(Nparticles)

print(m)

for i in range(0, Nparticles):
    m[i] = 1.0
    q[i] = 1.0
    x[i] = 0.5 * i
    v[i] = 0.2 * i
    T[i] = 0.5*m[i]*v[i]**2
    
print(m)
print(q)
print(x)
print(v)
print(T)
