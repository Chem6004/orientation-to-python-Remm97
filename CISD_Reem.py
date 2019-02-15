import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

r_array = np.linspace(0.5, 3.5, 20)*1.88973
print(r_array)

E_array = [-107.1389493226, -110.8762342308, -112.2035650482, -112.6221628016, -112.6993448642, -112.6532021548,-112.5695515418, -112.4825450847, -112.4093307577, -112.3611216888, -112.3328706063, -112.3154788092, -112.3040496673, -112.0685479896, -112.2907699794, -112.2869226228, -112.0012243902, -111.9483767861, -111.9274012790, -112.2798664306]
print(E_array)

plt.plot(r_array, E_array, 'red')
plt.show()

order = 3
sE = InterpolatedUnivariateSpline(r_array, E_array, k=order)
r_fine = np.linspace(1.06,5.0,200)
E_fine = sE(r_fine)
plt.plot(r_fine, E_fine, 'blue')
plt.show()

fE = sE.derivative()
F_fine = -1*fE(r_fine)

plt.plot(r_fine, np.abs(F_fine), 'black')
plt.xlim(1,5)
plt.show()

r_eq_idx = np.argmin(E_fine)
r_eq = r_fine[r_eq_idx]

print("Equilibrium bond length is ", r_eq," atomic units.")
print("Equilibrium bond length is ", r_eq*0.529," Angstroms.")

cE = fE.derivative()
k = cE(r_eq)
mu = 13625.
v = np.sqrt( np.sqrt(k/mu)/(2*mu))
r_init = np.random.uniform(0.75*r_eq,2*r_eq)
v_init = np.random.uniform(-2*v,2*v)

print("Initial separation is ",r_init, "atomic units.")
print("Initial velocity is ",v_init, "atomic units.")

dt = 0.02

F_init = -1*fE(r_init)

def Velocity_Verlet(r_curr, v_curr, mu, f_interp, dt):
    a_curr = -1*f_interp(r_curr)/mu
    r_fut = r_curr + v_curr * dt + 0.5 * a_curr * dt**2
    
    
    ### use r_fut to get future acceleration a_fut
    ''' STUDENT WRITTEN CODE GOES HERE!'''
    #a_fut = 
    ### use current and future acceleration to get future velocity v_fut
    ''' STUDENT WRITTEN CODE GOES HERE!'''
    #v_fut = 
    
    result = [r_fut, v_fut]
    return result

N_updates = 200000
r_vs_t = np.zeros(N_updates)
v_vs_t = np.zeros(N_updates)
t_array = np.zeros(N_updates)

r_vs_t[0] = r_init
v_vs_t[0] = v_init

result_array = Velocity_Verlet(r_init, v_init, mu, fE, dt)

for i in range(1,N_updates):
    tmp = Velocity_Verlet(result_array[0], result_array[1], mu, fE, dt)
    result_array = tmp
    t_array[i] = dt*i
    r_vs_t[i] = result_array[0]
    v_vs_t[i] = result_array[1]
    
plt.plot(t_array, r_vs_t, 'red')
plt.show()

plt.plot(mu*v_vs_t, r_vs_t, 'blue')
plt.show()

