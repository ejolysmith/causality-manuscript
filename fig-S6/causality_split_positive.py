from matplotlib import pylab as plt
import uncertainties as un
import pickle
import numpy as np

path_to_statistics = '../data/delta/final_statistics/'

# Load the data
with open(path_to_statistics + 'EJS3_0p1mMIPTG_split.pkl', 'rb') as f:
    data_EJS3_0p1mMIPTG = pickle.load(f)

with open(path_to_statistics + 'EJS3_0p5mMIPTG_split.pkl', 'rb') as f:
    data_EJS3_0p5mMIPTG = pickle.load(f)

with open(path_to_statistics + 'EJS4_split.pkl', 'rb') as f:
    data_EJS4 = pickle.load(f)

with open(path_to_statistics + 'EJS6_split.pkl', 'rb') as f:
    data_EJS6 = pickle.load(f)

# Convert data to uncertainties
etaxz_EJS3_0p1mM_IPTG = un.ufloat(data_EJS3_0p1mMIPTG['etaxz'], data_EJS3_0p1mMIPTG['etaxz_err'])
etayz_EJS3_0p1mM_IPTG = un.ufloat(data_EJS3_0p1mMIPTG['etayz'], data_EJS3_0p1mMIPTG['etayz_err'])

etaxz_EJS3_0p5mM_IPTG = un.ufloat(data_EJS3_0p5mMIPTG['etaxz'], data_EJS3_0p5mMIPTG['etaxz_err'])
etayz_EJS3_0p5mM_IPTG = un.ufloat(data_EJS3_0p5mMIPTG['etayz'], data_EJS3_0p5mMIPTG['etayz_err'])

etaxz_EJS4 = un.ufloat(data_EJS4['etaxz'], data_EJS4['etaxz_err'])
etayz_EJS4 = un.ufloat(data_EJS4['etayz'], data_EJS4['etayz_err'])

etaxz_EJS6 = un.ufloat(data_EJS6['etaxz'], data_EJS6['etaxz_err'])
etayz_EJS6 = un.ufloat(data_EJS6['etayz'], data_EJS6['etayz_err'])

# Plotting
a = 1.5
fig, (ax1, ax2) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [a, 1]})
fig.subplots_adjust(wspace=0.)

markersize = 11
rfpcolor = 'darkorange'
marker = 'o'
fs = 7

ax1.set_xlim(-0.01, -0.01 + (0.1+0.01)*(a/(a + 1)))
ax1.set_ylim(-0.01, 0.1)
ax1.spines['right'].set_visible(False)
ax1.set_xticks([0.0, 0.01, 0.02, 0.03, 0.04, 0.05])
ax1.set_yticks([0.0, 0.01, 0.02, 0.03, 0.04, 0.05])

ax2.set_xlim(-0.7 + (0.5 + 0.7)*(a/(1+a)), 0.5)
ax2.set_ylim(-0.7, 0.5)

ax2.spines['left'].set_visible(False)
ax2.yaxis.tick_right()
ax2.tick_params(labelleft=False)
ax2.set_xticks([0.1,0.2, 0.3, 0.4, 0.5])
ax2.set_yticks([0.1,0.2, 0.3, 0.4, 0.5])

d = .015  # size of diagonal break marks

# X breaks
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
ax1.plot([1-d, 1+d], [-d, +d], **kwargs)
ax1.plot([1-d, 1+d], [1-d, 1+d], **kwargs)

kwargs.update(transform=ax2.transAxes)
ax2.plot([-d, +d], [-d, +d], **kwargs)
ax2.plot([-d, +d], [1-d, 1+d], **kwargs)

# Y breaks
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
ax1.plot([-d, +d], [a/(a+1)-d , a/(a+1)+d], **kwargs)
#ax1.plot([-d, +d], [-d, +d], **kwargs)

kwargs.update(transform=ax2.transAxes)
ax1.plot([1-d, 1+d], [1-d, 1+d], **kwargs)
#ax1.plot([1-d, 1+d], [-d, +d], **kwargs)

# Diagonal y = x line
x1 = np.linspace(ax1.get_xlim()[0], ax1.get_xlim()[1], 100)
x2 = np.linspace(ax2.get_xlim()[0], ax2.get_xlim()[1], 100)
ax1.plot(x1, x1, '--', color='0.3', label = 'Eq. (2)')
ax2.plot(x2, x2, '--', color='0.3', label = 'Eq. (2)')

def plot_point(ax, x, y, index, label):
    ax.errorbar(x.nominal_value, y.nominal_value,
                xerr=x.std_dev, yerr=y.std_dev,
                fmt=marker, color=rfpcolor, markerfacecolor='white',
                markersize=markersize, label = label)
    ax.text(x.nominal_value, y.nominal_value, str(index),
            ha='center', va='center', color=rfpcolor, fontsize=fs)

system_index = 1
plot_point(ax1, etaxz_EJS3_0p1mM_IPTG, etayz_EJS3_0p1mM_IPTG, 1, "z = [rfp]")

system_index = 2
plot_point(ax1, etaxz_EJS3_0p5mM_IPTG, etayz_EJS3_0p5mM_IPTG, 2, None)

system_index = 3
plot_point(ax2, etaxz_EJS4, etayz_EJS4, 3, None)

system_index = 4
plot_point(ax2, etaxz_EJS6, etayz_EJS6, 4, "z = [rfp]")

# Labels
fig.text(0.5, 0.0, r'Normalized covariance $\eta_{xz}$', ha='center', fontsize=14)
fig.text(0.0, 0.5, r'Normalized covariance $\eta_{yz}$', va='center', rotation='vertical', fontsize=14)
plt.legend(loc = (0.3,0.2))

plt.show()

