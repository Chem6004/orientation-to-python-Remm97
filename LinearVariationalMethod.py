import numpy as np
import sympy as sp

def H_ij(i,j):
    a = (2/10)*(np.sin((i*np.pi)/2)*np.sin((j*np.pi)/2))
    b = (((np.pi**2)*(j**2))/((1000)))
    x = sp.Symbol('x')
    c = np.sin((i*np.pi*x)/10)
    d = np.sin((j*np.pi*x)/10)
    e = sp.integrate((c)*(d), x)
    ham_int = a+(b*e)
    
    if i==j:
        e = 0
    
    else:
        e = 1
    
    return ham_int

H_mat = np.zeros((3,3))

for i in range(0,3):
    for j in range(0,3):
        H_mat[i][j] = H_ij(i,j)
        
print(H_mat)