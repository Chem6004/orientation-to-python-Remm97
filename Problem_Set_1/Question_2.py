import numpy as np
### Function to return integrals involving Hamiltonian and basis functions
def H_ij(i, j):
    i = i+1
    j = j+1
    if i==j:
        ham_int = ((np.pi**2 * j**2)/2) - (1/3) - ((np.pi*j*np.sin(2*np.pi*j))/4) - (np.sin(2*np.pi*j)/(6*np.pi*j))
    else:
        ham_int = ((np.pi**2)*(j**2)) * np.sin(i*np.pi) *np.sin(j*np.pi) - (1/3) * np.sin(i*np.pi) *np.sin(j*np.pi)
        #(2) * np.sin(i*np.pi) * np.sin(j*np.pi)
        

    return ham_int

H_mat = np.zeros((3,3))

### loop over indices of the basis you are expanding in
### and compute and store the corresponding Hamiltonian matrix elements
for i in range(0,3):
    for j in range(0,3):
        H_mat[i][j] = H_ij(i, j)

### Print the resulting Hamiltonian matrix
print(H_mat)

### create an empty numpy array for the c vector
c = np.zeros(3)
### assign c vector to be (1, 0, 0)
c[0] = 0
c[1] = 0
c[2] = 1

### compute H_mat * c and store it to a new array called Hc
Hc = np.dot(H_mat,c)

### compute c^t * Hc and store it to a variable E
E = np.dot(np.transpose(c),Hc)

### print the result
print(E)

### compute eigenvalues and eigenvectors of H_mat
### store eigenvalues to E_opt and eigenvectors to c_opt
E_opt, c_opt = np.linalg.eig(H_mat)

### print lowest eigenvalues corresponding to the 
### variational estimate of the ground state energy
print("Ground state energy with potential is approximately ",E_opt)
print("Ground state energy of PIB is ",np.pi**2/(200))

### print coefficients that define the trial wavefunction with the lowest eigenvalue
### which corresponds to the variational estimate of the ground state wavefunction
print(c_opt[0])