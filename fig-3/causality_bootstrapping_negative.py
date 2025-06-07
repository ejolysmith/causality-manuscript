import numpy as np
from matplotlib import pylab as plt
import uncertainties as un
import pickle

path_to_statistics = '../data/delta/final_statistics/'

#EJS1
with open(path_to_statistics + 'EJS1_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS1 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS1 = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_EJS1 = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_EJS1 = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_EJS1 = data['generation_time']



#EJS2
with open(path_to_statistics + 'EJS2_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS2 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS2 = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_EJS2 = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_EJS2 = un.ufloat(data['etayg'], data['etayg_err'])
generation_EJS2 = data['generation_time']


#EJS7
with open(path_to_statistics + 'EJS7_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_EJS7 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_EJS7 = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_EJS7 = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_EJS7 = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_EJS7 = data['generation_time']



#PA52 with normal MC media:
with open(path_to_statistics + 'PA52_normalMC_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_PA52_normalMC = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA52_normalMC = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA52_normalMC = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA52_normalMC = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA52_normalMC = data['generation_time']


#PA52 with 0.5uM IPTG from experiment:
with open(path_to_statistics + 'PA52_0p5uMIPTG_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_PA52_0p5uM_IPTG = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA52_0p5uM_IPTG = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA52_0p5uM_IPTG = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA52_0p5uM_IPTG = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA52_0p5uM_IPTG = data['generation_time']


#PA52 with  2uM IPTG:
with open(path_to_statistics + 'PA52_2uMIPTG_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_PA52_2uM_IPTG = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA52_2uM_IPTG = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA52_2uM_IPTG = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA52_2uM_IPTG = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA52_2uM_IPTG = data['generation_time']



#PA53 with normal MC :
with open(path_to_statistics + 'PA53_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
    
etaxz_PA53 = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA53 = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA53 = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA53 = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA53 = data['generation_time']



#PA52 with 1uM IPTG:
with open(path_to_statistics + 'PA52_1uMIPTG_bootstrapping.pkl', 'rb') as f:
    data = pickle.load(f)
etaxz_PA52_1uM_IPTG = un.ufloat(data['etaxz'], data['etaxz_err'])
etayz_PA52_1uM_IPTG  = un.ufloat(data['etayz'], data['etayz_err'])
etaxg_PA52_1uM_IPTG = un.ufloat(data['etaxg'], data['etaxg_err'])
etayg_PA52_1uM_IPTG  = un.ufloat(data['etayg'], data['etayg_err'])
generation_time_PA52_1uM_IPTG  = data['generation_time']



x = np.linspace(-1, 1, 1000)


plt.plot(x,x, '--', color = '0.3', label = 'Eq. (2)')
markersize = 10
rfpcolor = 'darkblue'
growthratecolor = 'k'

fs = 7
marker = 's'
gmfc = '0.95'

system_index = 5
plt.errorbar(etaxz_EJS1.nominal_value, etayz_EJS1.nominal_value , xerr = etaxz_EJS1.std_dev, yerr = etayz_EJS1.std_dev, fmt = 's', color = rfpcolor, marker = marker, markerfacecolor = 'white', markersize = markersize)#, label = "No causality")
plt.text(etaxz_EJS1.nominal_value, etayz_EJS1.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_EJS1.nominal_value, etayg_EJS1.nominal_value , xerr = etaxg_EJS1.std_dev, yerr = etayg_EJS1.std_dev, fmt = 's', color = growthratecolor, marker = marker,markerfacecolor = gmfc ,markersize = markersize)#, label = "No causality")
plt.text(etaxg_EJS1.nominal_value, etayg_EJS1.nominal_value ,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)

system_index = 12
plt.errorbar(etaxz_EJS2.nominal_value, etayz_EJS2.nominal_value , xerr = etaxz_EJS2.std_dev, yerr = etayz_EJS2.std_dev, fmt = 's', color = rfpcolor, markersize = markersize,markerfacecolor = 'white',)#, label = "No causality?")
plt.text(etaxz_EJS2.nominal_value, etayz_EJS2.nominal_value ,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_EJS2.nominal_value, etayg_EJS2.nominal_value , xerr = etaxg_EJS2.std_dev, yerr = etayg_EJS2.std_dev, fmt = 's',color = growthratecolor, marker = marker,markerfacecolor = gmfc, markersize = markersize)#, label = "No causality?")
plt.text(etaxg_EJS2.nominal_value, etayg_EJS2.nominal_value,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)


system_index = 6
plt.errorbar(etaxz_PA52_normalMC.nominal_value, etayz_PA52_normalMC.nominal_value , xerr = etaxz_PA52_normalMC.std_dev, yerr = etayz_PA52_normalMC.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text( etaxz_PA52_normalMC.nominal_value, etayz_PA52_normalMC.nominal_value , system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA52_normalMC.nominal_value, etayg_PA52_normalMC.nominal_value , xerr = etaxg_PA52_normalMC.std_dev, yerr = etayg_PA52_normalMC.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)#, label = "No causality")
plt.text( etaxg_PA52_normalMC.nominal_value, etayg_PA52_normalMC.nominal_value  , system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)

system_index = 7
plt.errorbar(etaxz_PA52_0p5uM_IPTG.nominal_value, etayz_PA52_0p5uM_IPTG.nominal_value , xerr = etaxz_PA52_0p5uM_IPTG.std_dev, yerr = etayz_PA52_0p5uM_IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text(etaxz_PA52_0p5uM_IPTG.nominal_value, etayz_PA52_0p5uM_IPTG.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA52_0p5uM_IPTG.nominal_value, etayg_PA52_0p5uM_IPTG.nominal_value , xerr = etaxg_PA52_0p5uM_IPTG.std_dev, yerr = etayg_PA52_0p5uM_IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)#, label = "No causality")
plt.text(etaxg_PA52_0p5uM_IPTG.nominal_value, etayg_PA52_0p5uM_IPTG.nominal_value,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)


system_index = 8
plt.errorbar(etaxz_PA52_1uM_IPTG.nominal_value, etayz_PA52_1uM_IPTG.nominal_value , xerr = etaxz_PA52_1uM_IPTG.std_dev, yerr = etayz_PA52_1uM_IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white', markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text(etaxz_PA52_1uM_IPTG.nominal_value, etayz_PA52_1uM_IPTG.nominal_value, system_index,ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA52_1uM_IPTG.nominal_value, etayg_PA52_1uM_IPTG.nominal_value , xerr = etaxg_PA52_1uM_IPTG.std_dev, yerr = etayg_PA52_1uM_IPTG.std_dev,  fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)
plt.text( etaxg_PA52_1uM_IPTG.nominal_value, etayg_PA52_1uM_IPTG.nominal_value , system_index,ha="center", va="center", color = growthratecolor, fontsize = fs)


system_index = 9
plt.errorbar(etaxz_PA52_2uM_IPTG.nominal_value, etayz_PA52_2uM_IPTG.nominal_value , xerr = etaxz_PA52_2uM_IPTG.std_dev, yerr = etayz_PA52_2uM_IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor, label = "z = [rfp]")
plt.text( etaxz_PA52_2uM_IPTG.nominal_value, etayz_PA52_2uM_IPTG.nominal_value, system_index,ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA52_2uM_IPTG.nominal_value, etayg_PA52_2uM_IPTG.nominal_value , xerr = etaxg_PA52_2uM_IPTG.std_dev, yerr = etayg_PA52_2uM_IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc ,markersize = markersize, color = growthratecolor, label = "z = growth rate")
plt.text( etaxg_PA52_2uM_IPTG.nominal_value, etayg_PA52_2uM_IPTG.nominal_value , system_index,ha="center", va="center", color = growthratecolor, fontsize = fs)


system_index = 10
plt.errorbar(etaxz_PA53.nominal_value, etayz_PA53.nominal_value , xerr = etaxz_PA53.std_dev, yerr = etayz_PA53.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text(etaxz_PA53.nominal_value, etayz_PA53.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA53.nominal_value, etayg_PA53.nominal_value , xerr = etaxg_PA53.std_dev, yerr = etayg_PA53.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)#, label = "No causality")
plt.text(etaxg_PA53.nominal_value, etayg_PA53.nominal_value ,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)


system_index = 11
plt.errorbar(etaxz_EJS7.nominal_value, etayz_EJS7.nominal_value , xerr = etaxz_EJS7.std_dev, yerr = etayz_EJS7.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text(etaxz_EJS7.nominal_value, etayz_EJS7.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_EJS7.nominal_value, etayg_EJS7.nominal_value , xerr = etaxg_EJS7.std_dev, yerr = etayg_EJS7.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)#, label = "No causality")
plt.text(etaxg_EJS7.nominal_value, etayg_EJS7.nominal_value,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)


plt.xlim([-0.06,0.16])
plt.ylim([-0.06,0.16])
plt.yticks([0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15])
plt.legend(loc = (0.6,0.2))
plt.xlabel(r'Normalized covariance $\eta_{xz}$', fontsize = 14)
plt.ylabel(r'Normalized covariance $\eta_{yz}$', fontsize = 14)

plt.tight_layout()



