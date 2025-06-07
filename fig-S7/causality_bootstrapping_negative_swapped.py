import numpy as np
from matplotlib import pylab as plt
import uncertainties as un
import pickle

path_to_statistics = '../data/delta/final_statistics/'



with open(path_to_statistics + 'EJS9_repeat_bootstrapping.pkl', 'rb') as f:
    data_EJstrain9 = pickle.load(f)
    
etaxz_strain9_MM4 = un.ufloat(data_EJstrain9['etaxz'], data_EJstrain9['etaxz_err'])
etayz_strain9_MM4 = un.ufloat(data_EJstrain9['etayz'], data_EJstrain9['etayz_err'])
etaxg_strain9_MM4 = un.ufloat(data_EJstrain9['etaxg'], data_EJstrain9['etaxg_err'])
etayg_strain9_MM4 = un.ufloat(data_EJstrain9['etayg'], data_EJstrain9['etayg_err'])
generation_time_strain9_MM4 = data_EJstrain9['generation_time']


with open(path_to_statistics + 'EJS9_bootstrapping.pkl', 'rb') as f:
    data_EJstrain9_MM5 = pickle.load(f)
    
etaxz_strain9_MM5 = un.ufloat(data_EJstrain9_MM5['etaxz'], data_EJstrain9_MM5['etaxz_err'])
etayz_strain9_MM5 = un.ufloat(data_EJstrain9_MM5['etayz'], data_EJstrain9_MM5['etayz_err'])
etaxg_strain9_MM5 = un.ufloat(data_EJstrain9_MM5['etaxg'], data_EJstrain9_MM5['etaxg_err'])
etayg_strain9_MM5 = un.ufloat(data_EJstrain9_MM5['etayg'], data_EJstrain9_MM5['etayg_err'])
generation_time_strain9_MM5 = data_EJstrain9_MM5['generation_time']





x = np.linspace(-1, 1, 1000)


plt.plot(x,x, '--', color = '0.3', label = 'Eq. (2)')
markersize = 10
rfpcolor = 'darkblue'
growthratecolor = 'k'

fs = 7
marker = 's'
gmfc = '0.95'

system_index = 14
plt.errorbar(etaxz_strain9_MM4.nominal_value, etayz_strain9_MM4.nominal_value , xerr = etayz_strain9_MM4.std_dev, yerr = etayz_strain9_MM4.std_dev, fmt = 's', color = rfpcolor, marker = marker, markerfacecolor = 'white', markersize = markersize)#, label = "No causality")
plt.text(etaxz_strain9_MM4.nominal_value, etayz_strain9_MM4.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_strain9_MM4.nominal_value, etayg_strain9_MM4.nominal_value , xerr = etaxg_strain9_MM4.std_dev, yerr = etayg_strain9_MM4.std_dev, fmt = 's', color = growthratecolor, marker = marker,markerfacecolor = gmfc ,markersize = markersize)#, label = "No causality")
plt.text(etaxg_strain9_MM4.nominal_value, etayg_strain9_MM4.nominal_value ,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)


system_index = 14
plt.errorbar(etaxz_strain9_MM5.nominal_value, etayz_strain9_MM5.nominal_value , xerr = etayz_strain9_MM5.std_dev, yerr = etayz_strain9_MM5.std_dev, fmt = 's', color = rfpcolor, marker = marker, markerfacecolor = 'white', markersize = markersize)#, label = "No causality")
plt.text(etaxz_strain9_MM5.nominal_value, etayz_strain9_MM5.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_strain9_MM5.nominal_value, etayg_strain9_MM5.nominal_value , xerr = etaxg_strain9_MM5.std_dev, yerr = etayg_strain9_MM5.std_dev, fmt = 's', color = growthratecolor, marker = marker,markerfacecolor = gmfc ,markersize = markersize)#, label = "No causality")
plt.text(etaxg_strain9_MM5.nominal_value, etayg_strain9_MM5.nominal_value ,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)




plt.xlim([-0.06,0.16])
plt.ylim([-0.06,0.16])
plt.legend(loc = (0.6,0.2))
plt.xlabel(r'Normalized covariance $\eta_{xz}$', fontsize = 14)
plt.ylabel(r'Normalized covariance $\eta_{yz}$', fontsize = 14)

plt.tight_layout()



