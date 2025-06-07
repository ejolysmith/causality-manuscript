import numpy as np
from matplotlib import pylab as plt
import uncertainties as un
import pickle

path_to_statistics = '../data/thresholding/thresholding_final_statistics/'

#Strain 1 from EJMM2:
with open(path_to_statistics + 'EJS1_thresholding.pkl', 'rb') as f:
    data_EJstrain1 = pickle.load(f)
    
etaxz_strain1 = un.ufloat(data_EJstrain1['etaxz'], data_EJstrain1['etaxz_err'])
etayz_strain1 = un.ufloat(data_EJstrain1['etayz'], data_EJstrain1['etayz_err'])
etaxg_strain1 = un.ufloat(data_EJstrain1['etaxg'], data_EJstrain1['etaxg_err'])
etayg_strain1 = un.ufloat(data_EJstrain1['etayg'], data_EJstrain1['etayg_err'])




#Strain 2 from EJMM2:
with open(path_to_statistics + 'EJS2_thresholding.pkl', 'rb') as f:
    data_EJstrain2_normalMC = pickle.load(f)
    
etaxz_strain2_normalMC = un.ufloat(data_EJstrain2_normalMC['etaxz'], data_EJstrain2_normalMC['etaxz_err'])
etayz_strain2_normalMC = un.ufloat(data_EJstrain2_normalMC['etayz'], data_EJstrain2_normalMC['etayz_err'])
etaxg_strain2_normalMC = un.ufloat(data_EJstrain2_normalMC['etaxg'], data_EJstrain2_normalMC['etaxg_err'])
etayg_strain2_normalMC= un.ufloat(data_EJstrain2_normalMC['etayg'], data_EJstrain2_normalMC['etayg_err'])






#Strain 7 from EJMM4:
with open(path_to_statistics + 'EJS7_thresholding.pkl', 'rb') as f:
    data_EJstrain7mut = pickle.load(f)
    
etaxz_strain7_mut = un.ufloat(data_EJstrain7mut['etaxz'], data_EJstrain7mut['etaxz_err'])
etayz_strain7_mut = un.ufloat(data_EJstrain7mut['etayz'], data_EJstrain7mut['etayz_err'])
etaxg_strain7_mut = un.ufloat(data_EJstrain7mut['etaxg'], data_EJstrain7mut['etaxg_err'])
etayg_strain7_mut = un.ufloat(data_EJstrain7mut['etayg'], data_EJstrain7mut['etayg_err'])




#PA52 with normal MC with 0.5uM IPTG from experiment PAMM27:
with open(path_to_statistics + 'PA52_0p5uMIPTG_thresholding.pkl', 'rb') as f:
    data_PA52_normalMC_0p5IPTG = pickle.load(f)
    
etaxz_PA52_normalMC_0p5IPTG = un.ufloat(data_PA52_normalMC_0p5IPTG['etaxz'], data_PA52_normalMC_0p5IPTG['etaxz_err'])
etayz_PA52_normalMC_0p5IPTG = un.ufloat(data_PA52_normalMC_0p5IPTG['etayz'], data_PA52_normalMC_0p5IPTG['etayz_err'])
etaxg_PA52_normalMC_0p5IPTG = un.ufloat(data_PA52_normalMC_0p5IPTG['etaxg'], data_PA52_normalMC_0p5IPTG['etaxg_err'])
etayg_PA52_normalMC_0p5IPTG = un.ufloat(data_PA52_normalMC_0p5IPTG['etayg'], data_PA52_normalMC_0p5IPTG['etayg_err'])








#PA52 with normal MC with 2uM IPTG from experiment PAMM27:
with open(path_to_statistics + 'PA52_2uMIPTG_thresholding.pkl', 'rb') as f:
    data_PA52_normalMC_2IPTG = pickle.load(f)
    
etaxz_PA52_normalMC_2IPTG = un.ufloat(data_PA52_normalMC_2IPTG['etaxz'], data_PA52_normalMC_2IPTG['etaxz_err'])
etayz_PA52_normalMC_2IPTG = un.ufloat(data_PA52_normalMC_2IPTG['etayz'], data_PA52_normalMC_2IPTG['etayz_err'])
etaxg_PA52_normalMC_2IPTG = un.ufloat(data_PA52_normalMC_2IPTG['etaxg'], data_PA52_normalMC_2IPTG['etaxg_err'])
etayg_PA52_normalMC_2IPTG = un.ufloat(data_PA52_normalMC_2IPTG['etayg'], data_PA52_normalMC_2IPTG['etayg_err'])



#PA53 with normal MC  from experiment PAMM27:
with open(path_to_statistics + 'PA53_thresholding.pkl', 'rb') as f:
    data_PA53_normalMC = pickle.load(f)
    
etaxz_PA53 = un.ufloat(data_PA53_normalMC['etaxz'], data_PA53_normalMC['etaxz_err'])
etayz_PA53 = un.ufloat(data_PA53_normalMC['etayz'], data_PA53_normalMC['etayz_err'])
etaxg_PA53 = un.ufloat(data_PA53_normalMC['etaxg'], data_PA53_normalMC['etaxg_err'])
etayg_PA53 = un.ufloat(data_PA53_normalMC['etayg'], data_PA53_normalMC['etayg_err'])


#PA52 with normal MC from experiment PAMM26:
with open(path_to_statistics + 'PA52_normalMC_thresholding.pkl', 'rb') as f:
    data_PA52_normalMC = pickle.load(f)
    
etaxz_PA52_normalMC = un.ufloat(data_PA52_normalMC['etaxz'], data_PA52_normalMC['etaxz_err'])
etayz_PA52_normalMC = un.ufloat(data_PA52_normalMC['etayz'], data_PA52_normalMC['etayz_err'])
etaxg_PA52_normalMC = un.ufloat(data_PA52_normalMC['etaxg'], data_PA52_normalMC['etaxg_err'])
etayg_PA52_normalMC = un.ufloat(data_PA52_normalMC['etayg'], data_PA52_normalMC['etayg_err'])



#PA52 with normal MC and 1uM IPTG from experiment PAMM35:
with open(path_to_statistics + 'PA52_1uMIPTG_thresholding.pkl', 'rb') as f:
    data_PA52_normalMC_1IPTG = pickle.load(f)
etaxz_PA52_normalMC_1IPTG = un.ufloat(data_PA52_normalMC_1IPTG['etaxz'], data_PA52_normalMC_1IPTG['etaxz_err'])
etayz_PA52_normalMC_1IPTG = un.ufloat(data_PA52_normalMC_1IPTG['etayz'], data_PA52_normalMC_1IPTG['etayz_err'])
etaxg_PA52_normalMC_1IPTG = un.ufloat(data_PA52_normalMC_1IPTG['etaxg'], data_PA52_normalMC_1IPTG['etaxg_err'])
etayg_PA52_normalMC_1IPTG = un.ufloat(data_PA52_normalMC_1IPTG['etayg'], data_PA52_normalMC_1IPTG['etayg_err'])


x = np.linspace(-1, 1, 1000)


plt.plot(x,x, '--', color = '0.3', label = 'Eq. (2)')
markersize = 10
rfpcolor = 'darkblue'
growthratecolor = 'k'

fs = 7
marker = 's'
gmfc = '0.95'

system_index = 5
plt.errorbar(etaxz_strain1.nominal_value, etayz_strain1.nominal_value , xerr = etaxz_strain1.std_dev, yerr = etayz_strain1.std_dev, fmt = 's', color = rfpcolor, marker = marker, markerfacecolor = 'white', markersize = markersize)#, label = "No causality")
plt.text(etaxz_strain1.nominal_value, etayz_strain1.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_strain1.nominal_value, etayg_strain1.nominal_value , xerr = etaxg_strain1.std_dev, yerr = etayg_strain1.std_dev, fmt = 's', color = growthratecolor, marker = marker,markerfacecolor = gmfc ,markersize = markersize)#, label = "No causality")
plt.text(etaxg_strain1.nominal_value, etayg_strain1.nominal_value ,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)

system_index = 12
plt.errorbar(etaxz_strain2_normalMC.nominal_value, etayz_strain2_normalMC.nominal_value , xerr = etaxz_strain2_normalMC.std_dev, yerr = etayz_strain2_normalMC.std_dev, fmt = 's', color = rfpcolor, markersize = markersize,markerfacecolor = 'white',)#, label = "No causality?")
plt.text(etaxz_strain2_normalMC.nominal_value, etayz_strain2_normalMC.nominal_value ,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_strain2_normalMC.nominal_value, etayg_strain2_normalMC.nominal_value , xerr = etaxg_strain2_normalMC.std_dev, yerr = etayg_strain2_normalMC.std_dev, fmt = 's',color = growthratecolor, marker = marker,markerfacecolor = gmfc, markersize = markersize)#, label = "No causality?")
plt.text(etaxg_strain2_normalMC.nominal_value, etayg_strain2_normalMC.nominal_value,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)

system_index = 6
plt.errorbar(etaxz_PA52_normalMC.nominal_value, etayz_PA52_normalMC.nominal_value , xerr = etaxz_PA52_normalMC.std_dev, yerr = etayz_PA52_normalMC.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text( etaxz_PA52_normalMC.nominal_value, etayz_PA52_normalMC.nominal_value , system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA52_normalMC.nominal_value, etayg_PA52_normalMC.nominal_value , xerr = etaxg_PA52_normalMC.std_dev, yerr = etayg_PA52_normalMC.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)#, label = "No causality")
plt.text( etaxg_PA52_normalMC.nominal_value, etayg_PA52_normalMC.nominal_value  , system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)

system_index = 7
plt.errorbar(etaxz_PA52_normalMC_0p5IPTG.nominal_value, etayz_PA52_normalMC_0p5IPTG.nominal_value , xerr = etaxz_PA52_normalMC_0p5IPTG.std_dev, yerr = etayz_PA52_normalMC_0p5IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text(etaxz_PA52_normalMC_0p5IPTG.nominal_value, etayz_PA52_normalMC_0p5IPTG.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA52_normalMC_0p5IPTG.nominal_value, etayg_PA52_normalMC_0p5IPTG.nominal_value , xerr = etaxg_PA52_normalMC_0p5IPTG.std_dev, yerr = etayg_PA52_normalMC_0p5IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)#, label = "No causality")
plt.text(etaxg_PA52_normalMC_0p5IPTG.nominal_value, etayg_PA52_normalMC_0p5IPTG.nominal_value,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)

system_index = 8
plt.errorbar(etaxz_PA52_normalMC_1IPTG.nominal_value, etayz_PA52_normalMC_1IPTG.nominal_value , xerr = etaxz_PA52_normalMC_1IPTG.std_dev, yerr = etayz_PA52_normalMC_1IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white', markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text(etaxz_PA52_normalMC_1IPTG.nominal_value, etayz_PA52_normalMC_1IPTG.nominal_value, system_index,ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA52_normalMC_1IPTG.nominal_value, etayg_PA52_normalMC_1IPTG.nominal_value , xerr = etaxg_PA52_normalMC_1IPTG.std_dev, yerr = etayg_PA52_normalMC_1IPTG.std_dev,  fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)
plt.text( etaxg_PA52_normalMC_1IPTG.nominal_value, etayg_PA52_normalMC_1IPTG.nominal_value , system_index,ha="center", va="center", color = growthratecolor, fontsize = fs)


system_index = 9
plt.errorbar(etaxz_PA52_normalMC_2IPTG.nominal_value, etayz_PA52_normalMC_2IPTG.nominal_value , xerr = etaxz_PA52_normalMC_2IPTG.std_dev, yerr = etayz_PA52_normalMC_2IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor, label = "z = [rfp]")
plt.text( etaxz_PA52_normalMC_2IPTG.nominal_value, etayz_PA52_normalMC_2IPTG.nominal_value, system_index,ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA52_normalMC_2IPTG.nominal_value, etayg_PA52_normalMC_2IPTG.nominal_value , xerr = etaxg_PA52_normalMC_2IPTG.std_dev, yerr = etayg_PA52_normalMC_2IPTG.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc ,markersize = markersize, color = growthratecolor, label = "z = growth rate")
plt.text( etaxg_PA52_normalMC_2IPTG.nominal_value, etayg_PA52_normalMC_2IPTG.nominal_value , system_index,ha="center", va="center", color = growthratecolor, fontsize = fs)

system_index = 10
plt.errorbar(etaxz_PA53.nominal_value, etayz_PA53.nominal_value , xerr = etaxz_PA53.std_dev, yerr = etayz_PA53.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text(etaxz_PA53.nominal_value, etayz_PA53.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_PA53.nominal_value, etayg_PA53.nominal_value , xerr = etaxg_PA53.std_dev, yerr = etayg_PA53.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)#, label = "No causality")
plt.text(etaxg_PA53.nominal_value, etayg_PA53.nominal_value ,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)


system_index = 11
plt.errorbar(etaxz_strain7_mut.nominal_value, etayz_strain7_mut.nominal_value , xerr = etaxz_strain7_mut.std_dev, yerr = etayz_strain7_mut.std_dev, fmt = 's', marker = marker,markerfacecolor = 'white',markersize = markersize, color = rfpcolor)#, label = "No causality")
plt.text(etaxz_strain7_mut.nominal_value, etayz_strain7_mut.nominal_value,system_index, ha="center", va="center", color = rfpcolor, fontsize = fs)
plt.errorbar(etaxg_strain7_mut.nominal_value, etayg_strain7_mut.nominal_value , xerr = etaxg_strain7_mut.std_dev, yerr = etayg_strain7_mut.std_dev, fmt = 's', marker = marker,markerfacecolor = gmfc,markersize = markersize, color = growthratecolor)#, label = "No causality")
plt.text(etaxg_strain7_mut.nominal_value, etayg_strain7_mut.nominal_value,system_index, ha="center", va="center", color = growthratecolor, fontsize = fs)



plt.xlim([-0.09,0.19])
plt.ylim([-0.09,0.19])
plt.legend(loc = (0.6,0.2))
plt.xlabel(r'Normalized covariance $\eta_{xz}$', fontsize = 14)
plt.ylabel(r'Normalized covariance $\eta_{yz}$', fontsize = 14)

plt.tight_layout()



