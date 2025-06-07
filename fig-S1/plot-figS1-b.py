
import numpy as np
from matplotlib import pylab as plt


c1 = "simulated-etas.txt"

data = np.loadtxt(c1)



fig, axs = plt.subplots(1, 1)

axs.plot(data[:,2], data[:,0], '.', markersize = 10)
plt.xlabel('Feedback strength', fontsize = 20)
plt.ylabel(r'$\rho_{xz}/ \rho_{yz}$', fontsize = 20)
plt.yticks([0,0.5, 1, 1.5, 2] , fontsize = 15)
plt.xticks(fontsize = 15)
plt.ylim([0,2])


fig, axs = plt.subplots(1, 1)

axs.plot(data[:,2], data[:,1], '.', markersize = 10)
plt.xlabel('Feedback strength', fontsize = 20)
plt.ylabel(r'$\eta_{xz}/ \eta_{yz}$', fontsize = 20)
plt.yticks([0,0.5, 1, 1.5, 2] , fontsize = 15)
plt.xticks(fontsize = 15)
plt.ylim([0,2])
