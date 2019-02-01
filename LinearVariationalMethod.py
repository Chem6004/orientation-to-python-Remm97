import numpy as np

def H_ij(i,j):
    a = (2/10)*(np.sin((i*np.pi)/2)*np.sin((j*np.pi)/2))
    b = (((np.pi**2)*(j**2))/((200)))

    ham_int = a+b
    
    if i==j:
        ham_int = a+b
    
    else:
        ham_int = a
    
    return ham_int

H_mat = np.zeros((3,3))

for i in range(1,4):
    for j in range(1,4):
        H_mat[i-1][j-1] = H_ij(i,j)
        
print(H_mat)

c = np.zeros(3)

c[0] = 0
c[1] = 0
c[2] = np.sqrt(.5)

norm = np.dot(np.transpose(c), c)

Hc = np.dot(H_mat,c)

E = np.dot(np.transpose(c),Hc)/norm

print(E)