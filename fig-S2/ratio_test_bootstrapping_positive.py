import numpy as np
from matplotlib import pylab as plt
import uncertainties as un
import pickle

path_to_statistics = '../data/delta/final_statistics/'



with open(path_to_statistics + 'EJS3_0p1mMIPTG_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS3_0p1mM_IPTG = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS3_0p1mM_IPTG = un.ufloat(data['etayz'], data['etayz_err'])
generation_time_EJS3_0p1mM_IPTG = data['generation_time']
rz_EJS3_0p1mM_IPTG = etaxz_EJS3_0p1mM_IPTG/etayz_EJS3_0p1mM_IPTG



with open(path_to_statistics + 'EJS3_0p5mMIPTG_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS3_0p5mM_IPTG = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS3_0p5mM_IPTG = un.ufloat(data['etayz'], data['etayz_err'])
generation_time_EJS3_0p5mM_IPTG = data['generation_time']
rz_EJS3_0p5mM_IPTG = etaxz_EJS3_0p5mM_IPTG/etayz_EJS3_0p5mM_IPTG



with open(path_to_statistics + 'EJS4_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS4 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS4 = un.ufloat(data['etayz'], data['etayz_err'])
generation_time_EJS4 = data['generation_time']
rz_EJS4 = etaxz_EJS4/etayz_EJS4


with open(path_to_statistics + 'EJS6_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS6= un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS6= un.ufloat(data['etayz'], data['etayz_err'])
generation_time_EJS6= data['generation_time']
rz_EJS6= etaxz_EJS6/etayz_EJS6


markersize = 5
rfpcolor = 'darkorange'
growthratecolor = 'k'

fs = 7
marker = 'o'
gmfc = '0.95'


indexes = range(1,5)
plt.figure()
plt.plot(range(0,6), np.ones(len(range(0,6))), '--', color = '0.3', label = r'$\eta_{xz}/\eta_{yz} = 1$')

rz_plot = [rz_EJS3_0p1mM_IPTG.nominal_value, rz_EJS3_0p5mM_IPTG.nominal_value, rz_EJS4.nominal_value, rz_EJS6.nominal_value]
rz_plot_err = [rz_EJS3_0p1mM_IPTG.std_dev, rz_EJS3_0p5mM_IPTG.std_dev, rz_EJS4.std_dev, rz_EJS6.std_dev]
plt.errorbar(indexes, rz_plot, yerr = rz_plot_err, fmt = '.', color = rfpcolor, marker = marker, markerfacecolor = 'white', label = 'z = [rfp]')
plt.xlim([0, 5])
plt.ylim([-1,2])
plt.legend(loc = (0.72,0.15), fontsize = 14)
plt.xlabel('Synthetic circuit index', fontsize = 14)
plt.ylabel(r'Covariability ratio $\eta_{xz}/\eta_{yz}$', fontsize = 14)


