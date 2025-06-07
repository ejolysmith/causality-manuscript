
import numpy as np
from matplotlib import pylab as plt
import uncertainties as un
import pickle

path_to_statistics = '../data/delta/final_statistics/'

with open(path_to_statistics + 'EJS1_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS1 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS1 = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_EJS1 = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_EJS1 = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_EJS1 = data['generation_time']
rz_EJS1 = etaxz_EJS1/etayz_EJS1
rg_EJS1 = etaxg_EJS1/etayg_EJS1



with open(path_to_statistics + 'EJS2_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS2 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS2 = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_EJS2 = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_EJS2= un.ufloat(data['etayg'], data['etayg_err'])
generation_time_EJS2 = data['generation_time']
rz_EJS2 = etaxz_EJS2/etayz_EJS2
rg_EJS2 = etaxg_EJS2/etayg_EJS2



with open(path_to_statistics + 'EJS7_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS7 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS7 = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_EJS7 = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_EJS7 = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_EJS7 = data['generation_time']
rz_EJS7 = etaxz_EJS7/etayz_EJS7
rg_EJS7 = etaxg_EJS7/etayg_EJS7




with open(path_to_statistics + 'PA52_normalMC_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_PA52_normalMC = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA52_normalMC = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA52_normalMC = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA52_normalMC = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA52_normalMC = data['generation_time']
rz_PA52_normalMC = etaxz_PA52_normalMC/etayz_PA52_normalMC
rg_PA52_normalMC = etaxg_PA52_normalMC/etayg_PA52_normalMC


with open(path_to_statistics + 'PA52_0p5uMIPTG_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_PA52_0p5mM_IPTG = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA52_0p5mM_IPTG = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA52_0p5mM_IPTG = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA52_0p5mM_IPTG = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA52_0p5mM_IPTG = data['generation_time']
rz_PA52_0p5mM_IPTG = etaxz_PA52_0p5mM_IPTG/etayz_PA52_0p5mM_IPTG
rg_PA52_0p5mM_IPTG = etaxg_PA52_0p5mM_IPTG/etayg_PA52_0p5mM_IPTG


with open(path_to_statistics + 'PA52_2uMIPTG_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_PA52_2uM_IPTG = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA52_2uM_IPTG = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA52_2uM_IPTG = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA52_2uM_IPTG = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA52_2uM_IPTG = data['generation_time']
rz_PA52_2uM_IPTG = etaxz_PA52_2uM_IPTG/etayz_PA52_2uM_IPTG
rg_PA52_2uM_IPTG = etaxg_PA52_2uM_IPTG/etayg_PA52_2uM_IPTG



with open(path_to_statistics + 'PA53_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_PA53 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA53 = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA53 = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA53 = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA53 = data['generation_time']
rz_PA53 = etaxz_PA53/etayz_PA53
rg_PA53 = etaxg_PA53/etayg_PA53



with open(path_to_statistics + 'PA52_1uMIPTG_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
etaxz_PA52_1uM_IPTG = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA52_1uM_IPTG = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA52_1uM_IPTG = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA52_1uM_IPTG = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA52_1uM_IPTG = data['generation_time']
rz_PA52_1uM_IPTG = etaxz_PA52_1uM_IPTG/etayz_PA52_1uM_IPTG
rg_PA52_1uM_IPTG = etaxg_PA52_1uM_IPTG/etayg_PA52_1uM_IPTG

x = np.linspace(-1, 1, 1000)


markersize = 5
rfpcolor = 'darkblue'
growthratecolor = 'k'

fs = 7
marker = 's'
gmfc = '0.95'


indexes = range(5,13)
plt.figure()
plt.plot(range(4,15), np.ones(len(range(4,15))), '--', color = '0.3', label = r'$\eta_{xz}/\eta_{yz} = 1$')

rz_plot = [rz_EJS1.nominal_value, rz_PA52_normalMC.nominal_value, rz_PA52_0p5mM_IPTG.nominal_value, rz_PA52_1uM_IPTG.nominal_value, rz_PA52_2uM_IPTG.nominal_value, rz_PA53.nominal_value,  rz_EJS7.nominal_value, rz_EJS2.nominal_value]
rz_plot_err = [rz_EJS1.std_dev, rz_PA52_normalMC.std_dev, rz_PA52_0p5mM_IPTG.std_dev, rz_PA52_1uM_IPTG.std_dev, rz_PA52_2uM_IPTG.std_dev, rz_PA53.std_dev,  rz_EJS7.std_dev, rz_EJS2.std_dev]
plt.errorbar(indexes, rz_plot, yerr = rz_plot_err, fmt = '.', color = rfpcolor, marker = marker, markerfacecolor = 'white', label = 'z = [rfp]')
plt.xlim([4.5, 12.5])
plt.ylim([-5,6])
plt.legend(loc = (0.72,0.15), fontsize = 14)
plt.xlabel('Synthetic circuit index', fontsize = 14)
plt.ylabel(r'Covariability ratio $\eta_{xz}/\eta_{yz}$', fontsize = 14)


indexes = range(5,13)
plt.figure()

plt.plot(range(4,15), np.ones(len(range(4,15))), '--', color = '0.3', label = r'$\eta_{xz}/\eta_{yz} = 1$')

rg_plot = [rg_EJS1.nominal_value, rg_PA52_normalMC.nominal_value, rg_PA52_0p5mM_IPTG.nominal_value, rg_PA52_1uM_IPTG.nominal_value, rg_PA52_2uM_IPTG.nominal_value, rg_PA53.nominal_value,  rg_EJS7.nominal_value, rg_EJS2.nominal_value]
rg_plot_err = [rg_EJS1.std_dev, rg_PA52_normalMC.std_dev, rg_PA52_0p5mM_IPTG.std_dev, rg_PA52_1uM_IPTG.std_dev, rg_PA52_2uM_IPTG.std_dev, rg_PA53.std_dev,  rg_EJS7.std_dev, rg_EJS2.std_dev]
plt.errorbar(indexes, rg_plot, yerr = rg_plot_err, fmt = '.', color = growthratecolor, marker = marker, markerfacecolor = gmfc, label = 'z = growth rate')
plt.xlim([4.5, 12.5])
plt.ylim([-5,6])
plt.xlabel('Synthetic circuit index', fontsize = 14)
plt.legend(loc = (0.72,0.15), fontsize = 14)
plt.ylabel(r'Covariability ratio $\eta_{xz}/\eta_{yz}$', fontsize = 14)




plt.tight_layout()
