import numpy as np
from matplotlib import pylab as plt
import random


etaxz = np.array([])
etayz = np.array([])

for i in [1,2,3,4,5]:
    sys = str(i)
    c = "../simulations/fig-1-simulations/causal-" + sys + "/with-causality-data-system-" + sys + ".txt"
    data = np.loadtxt(c)
    etaxz = np.append(etaxz, data[:,0])
    etayz = np.append(etayz, data[:,1])
    

etaxz_final = [etaxz[0]]
etayz_final = [etayz[0]]


#density filter to keep dots not too clustered for illustration
d = 0.145
for i in range(len(etaxz)):
    d = 0.14 + 0.06*random.uniform(0, 1)
    A = 1
    for j in range(len(etaxz_final)):
        if ( etaxz[i]-etaxz_final[j] )**2 + (etayz[i]-etayz_final[j])**2 < d*d:
            A = 0
    if A == 1:
        etaxz_final.append(etaxz[i])
        etayz_final.append(etayz[i])
        
        
        
etaxz = np.array([])
etayz = np.array([])

for i in [1,2]:
    sys = str(i)
    c = "../simulations/fig-1-simulations/non-causal-" + sys + "/no-causality-data-system-" + sys + ".txt"
    data = np.loadtxt(c)
    etaxz = np.append(etaxz, data[:,0])
    etayz = np.append(etayz, data[:,1])
    
etaxz_final_no = [etaxz[7]]
etayz_final_no = [etayz[7]]

d = 0.1
for i in range(len(etaxz)):
    d = 0.08 + 0.08*random.uniform(0, 1)
    A = 1
    for j in range(len(etaxz_final_no)):
        if ( etaxz[i]-etaxz_final_no[j] )**2 + (etayz[i]-etayz_final_no[j])**2 < d*d:
            A = 0
    if A == 1:
        etaxz_final_no.append(etaxz[i])
        etayz_final_no.append(etayz[i])

        
plt.plot( etaxz_final, etayz_final,  '.', markersize = 14)
plt.plot(np.linspace(-1,1,100), np.linspace(-1,1,100), '--', linewidth = 3,  color = '0.5', label = 'Eq. (1)')
plt.plot( etaxz_final_no, etayz_final_no,  's', markersize = 10, color = 'mediumblue')

plt.xlim([-0.25,1])
plt.ylim([-0.25,1])

plt.xlabel(r'Normalized covariance $\eta_{xz_{i}}$', fontsize = 14)
plt.ylabel(r'Normalized covariance $\eta_{yz_{i}}$', fontsize = 14)



