import numpy as np
from matplotlib import pylab as plt
import uncertainties as un
import pickle


path_to_statistics = '../data/delta/final_statistics/'


#EJS2:
with open(path_to_statistics + 'EJS2_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS2 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS2 = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_EJS2 = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_EJS2 = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_EJS2 = data['generation_time']



path_to_statistics = '../data/delta/final_statistics/'
#Strain 2 from EJMM2:
with open(path_to_statistics + 'PA66_bootstrapping.pkl', 'rb') as f:
    data_PA66 = pickle.load(f)
    
etaxz_PA66 = un.ufloat(data_PA66['etaxz'], data_PA66['etaxz_err'])
etayz_PA66 = un.ufloat(data_PA66['etayz'], data_PA66['etayz_err'])
etaxg_PA66 = un.ufloat(data_PA66['etaxg'], data_PA66['etaxg_err'])
etayg_PA66= un.ufloat(data_PA66['etayg'], data_PA66['etayg_err'])
generation_time_PA66 = data_PA66['generation_time']






x = np.linspace(-1, 1, 1000)


plt.plot(x,x, '--', color = '0.3', label = 'Eq. (2)')
markersize = 10
rfpcolor = 'darkblue'
growthratecolor = 'k'

fs = 7
marker = 's'
gmfc = '0.95'


system_index = 12
plt.errorbar(etaxz_EJS2.nominal_value, etayz_EJS2.nominal_value , xerr = etaxz_EJS2.std_dev, yerr = etayz_EJS2.std_dev, fmt = 's', color = rfpcolor, markersize = markersize,markerfacecolor = 'white',)
plt.text(etaxz_EJS2.nominal_value, etayz_EJS2.nominal_value ,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_EJS2.nominal_value, etayg_EJS2.nominal_value , xerr = etaxg_EJS2.std_dev, yerr = etayg_EJS2.std_dev, fmt = 's',color = growthratecolor, marker = marker,markerfacecolor = gmfc, markersize = markersize)
plt.text(etaxg_EJS2.nominal_value, etayg_EJS2.nominal_value,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)



system_index = 13
plt.errorbar(etaxz_PA66.nominal_value, etayz_PA66.nominal_value , xerr = etaxz_PA66.std_dev, yerr = etayz_PA66.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor)
plt.text(etaxz_PA66.nominal_value, etayz_PA66.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA66.nominal_value, etayg_PA66.nominal_value , xerr = etaxg_PA66.std_dev, yerr = etayg_PA66.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)
plt.text(etaxg_PA66.nominal_value, etayg_PA66.nominal_value ,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)



plt.xlim([-0.06,0.16])
plt.ylim([-0.06,0.16])
plt.yticks([0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15])
plt.legend(loc = (0.6,0.2))
plt.xlabel(r'Normalized covariance $\eta_{xz}$', fontsize = 14)
plt.ylabel(r'Normalized covariance $\eta_{yz}$', fontsize = 14)

plt.tight_layout()
