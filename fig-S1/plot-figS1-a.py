import numpy as np
from matplotlib import pylab as plt
from matplotlib.ticker import NullFormatter


c1 = "system-simulation-data-1.txt"

data1 = np.loadtxt(c1)

a = 10000
T = 10000 + 1000
t = data1[:,0][a+1000:a + T]
x = data1[:,1][a+1000:a + T]
y = data1[:,2][a+1000:a + T]
z = data1[:,3][a+1000:a + T] + 3
fig, axs = plt.subplots(1, 1)
axs.plot(t, y, color = 'midnightblue', label = 'y')
axs.plot(t, x, color = 'lightsteelblue', label = 'x')
axs.set_ylim([0,33])
#axs1 = axs.twinx()
axs.plot(t, z, color = 'darkorange', linewidth = 3, label = 'z')
axs.set_ylim([0,33])
axs.set_xlabel('Time (arb. units)')
plt.xticks(  [ int(t[0]), int(t[int(len(t)/2)]), int(t[-1])]  , ['0','0.5','1'] )
axs.set_xlim(  [ int(t[0]), int(t[-1])]  )
plt.ylabel('Abundance')
plt.legend()
plt.show()



joint_kws=dict(gridsize=15)
joint = np.zeros([len(data1),2])
x = data1[:,3] + 3
y = data1[:,1]

# define some gridding.
axHist2d = plt.subplot2grid( (9,9), (1,0), colspan=8, rowspan=8 )
axHistx  = plt.subplot2grid( (9,9), (0,0), colspan=8 )
axHisty  = plt.subplot2grid( (9,9), (1,8), rowspan=8 )

xbins = int(np.max(x) - np.min(x))
ybins = int(np.max(y) - np.min(y))

H, xedges, yedges = np.histogram2d( x, y, bins=(xbins,ybins) )
axHist2d.imshow(H.T, interpolation='nearest', aspect='auto', cmap = 'Greys' )

axHistx.hist(x, bins=xedges, facecolor='lightsteelblue', alpha=0.8, edgecolor=None )
axHisty.hist(y, bins=yedges, facecolor='darkorange', alpha=0.5, orientation='horizontal', edgecolor=None)


axHistx.set_xlim( [xedges.min(), xedges.max()] )
axHisty.set_ylim( [yedges.min(), yedges.max()] )
axHist2d.set_ylim( [ axHist2d.get_ylim()[1], axHist2d.get_ylim()[0] ] )

nullfmt   = NullFormatter()
axHistx.xaxis.set_major_formatter(nullfmt)
axHistx.yaxis.set_major_formatter(nullfmt)
axHisty.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)
axHist2d.set_xlim( [ 4,18] )
axHistx.set_xlim( [ 7,21] )
axHist2d.set_ylim( [ 3,26] )
axHisty.set_ylim( [ 3,26] )
axHist2d.set_xticks([5, 10, 15])


axHistx.spines['top'].set_visible(False)
axHistx.spines['right'].set_visible(False)
axHistx.spines['left'].set_visible(False)
axHisty.spines['top'].set_visible(False)
axHisty.spines['bottom'].set_visible(False)
axHisty.spines['right'].set_visible(False)

axHistx.set_xticks([])
axHistx.set_yticks([])
axHisty.set_xticks([])
axHisty.set_yticks([])

axHist2d.tick_params(axis='both', which='major', labelsize=15)

axHist2d.set_xlabel('Z abundance', fontsize = 20)
axHist2d.set_ylabel('X abundance', fontsize = 20)

plt.show()





joint_kws=dict(gridsize=15)
joint = np.zeros([len(data1),2])
x = data1[:,3] + 3
y = data1[:,2]
#sns.jointplot(x = X, y = Y, kind="hex")

# define some gridding.
axHist2d = plt.subplot2grid( (9,9), (1,0), colspan=8, rowspan=8 )
axHistx  = plt.subplot2grid( (9,9), (0,0), colspan=8 )
axHisty  = plt.subplot2grid( (9,9), (1,8), rowspan=8 )

xbins = int(np.max(x) - np.min(x))
ybins = int(np.max(y) - np.min(y))

H, xedges, yedges = np.histogram2d( x, y, bins=(xbins,ybins) )
axHist2d.imshow(H.T, interpolation='nearest', aspect='auto', cmap = 'Greys' )

axHistx.hist(x, bins=xedges, facecolor='midnightblue', alpha=0.8, edgecolor=None )
axHisty.hist(y, bins=yedges, facecolor='darkorange', alpha=0.5, orientation='horizontal', edgecolor=None)


axHistx.set_xlim( [xedges.min(), xedges.max()] )
axHisty.set_ylim( [yedges.min(), yedges.max()] )
axHist2d.set_ylim( [ axHist2d.get_ylim()[1], axHist2d.get_ylim()[0] ] )

nullfmt   = NullFormatter()
axHistx.xaxis.set_major_formatter(nullfmt)
axHistx.yaxis.set_major_formatter(nullfmt)
axHisty.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)
axHist2d.set_xlim( [ 4,18] )
axHistx.set_xlim( [ 7,21] )
axHist2d.set_ylim( [ 3,26] )
axHisty.set_ylim( [ 3,26] )
axHist2d.set_xticks([5, 10, 15])


axHistx.spines['top'].set_visible(False)
axHistx.spines['right'].set_visible(False)
axHistx.spines['left'].set_visible(False)
axHisty.spines['top'].set_visible(False)
axHisty.spines['bottom'].set_visible(False)
axHisty.spines['right'].set_visible(False)

axHistx.set_xticks([])
axHistx.set_yticks([])
axHisty.set_xticks([])
axHisty.set_yticks([])

axHist2d.tick_params(axis='both', which='major', labelsize=15)

axHist2d.set_xlabel('Z abundance', fontsize = 20)
axHist2d.set_ylabel('Y abundance', fontsize = 20)

plt.show()