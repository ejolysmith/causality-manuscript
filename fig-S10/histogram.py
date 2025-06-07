import matplotlib.pyplot as plt
import numpy as np
import pickle
import uncertainties as un



path_to_statistics = '../data/delta/final_statistics_rpos_stuff/'

with open(path_to_statistics + 'PA12_bootstrapping.pkl', 'rb') as f:
    data_PA12 = pickle.load(f)
    
CVZ_PA12 = un.ufloat(data_PA12['CVz'], data_PA12['CVz_err'])
CVG_PA12 = un.ufloat(data_PA12['CVg'], data_PA12['CVg_err'])


with open(path_to_statistics + 'EJS1_bootstrapping.pkl', 'rb') as f:
    data_EJstrain1 = pickle.load(f)
    
CVZ_EJstrain1 = un.ufloat(data_EJstrain1['CVz'], data_EJstrain1['CVz_err'])
CVG_EJstrain1 = un.ufloat(data_EJstrain1['CVg'], data_EJstrain1['CVg_err'])


with open(path_to_statistics + 'EJS2_bootstrapping.pkl', 'rb') as f:
    data_EJstrain2 = pickle.load(f)
    
CVZ_EJstrain2 = un.ufloat(data_EJstrain2['CVz'], data_EJstrain2['CVz_err'])
CVG_EJstrain2 = un.ufloat(data_EJstrain2['CVg'], data_EJstrain2['CVg_err'])




CV1 = [CVZ_EJstrain2.nominal_value, CVG_EJstrain2.nominal_value]
CV1_ERRs = [CVZ_EJstrain2.std_dev, CVG_EJstrain2.std_dev]


CV2 = [CVZ_EJstrain1.nominal_value, CVG_EJstrain1.nominal_value]
CV2_ERRs = [CVZ_EJstrain1.std_dev, CVG_EJstrain1.std_dev]


CV3 = [CVZ_PA12.nominal_value, CVG_PA12.nominal_value]
CV3_ERRs = [CVZ_PA12.std_dev, CVG_PA12.std_dev]




fig = plt.figure()
ax = fig.add_subplot(111)

N = 2
ind = np.arange(N)            
width = 0.2     
aa = 1.2             # the width of the bars
fontsize = 15
## the bars
rects1 = ax.bar(ind, CV1, width,
                color='black',
                yerr=CV1_ERRs,
                error_kw=dict(elinewidth=2,ecolor='darkorange'), label = 'outlier')

rects2 = ax.bar(ind+width, CV2, width,
                    color='0.5',
                    yerr=CV2_ERRs,
                    error_kw=dict(elinewidth=2,ecolor='darkorange'), label = 'repressilator')

rects3 = ax.bar(ind+2*width, CV3, width,
                    color='0.8',
                    yerr=CV3_ERRs,
                    error_kw=dict(elinewidth=2,ecolor='darkorange'), label = 'no plasmid')


# axes and labels
ax.set_xlim(-width,len(ind) -0.1)
ax.set_ylabel('CV', fontsize = fontsize)
xTickMarks = ['rfp', 'growth rate']
ax.set_xticks([width, 6*width])
xtickNames = ax.set_xticklabels(xTickMarks, fontsize = fontsize)
plt.legend()
plt.tight_layout()
plt.show()
