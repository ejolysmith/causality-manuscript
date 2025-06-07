

import numpy as np
from matplotlib import pylab as plt


number_of_splits = 5



fig, ax = plt.subplots(figsize = (2.5,2.5))
color1 = 'xkcd:royal'
color2 = 'xkcd:pumpkin'
color3 = 'xkcd:teal blue' 
color4 = 'xkcd:rouge'
color5 = 'xkcd:light mauve'
color6 = '0.6'
colors = [color1, color2, color3, color4, color5, color6]
xxx = [-1,0,1]
ax.plot(xxx,xxx, '--', color = '0.7', zorder = 0)



color = colors[0]
for sys in [1,2,3,4,5,6,7,8,9,10]:  #4,5


    rhoxz_conc = np.array([])
    rhoxz_num  = np.array([])
    rhoxz_conc_err = np.array([])
    rhoxz_num_err  = np.array([])
    rhoyz_conc = np.array([])
    rhoyz_num  = np.array([])
    rhoyz_conc_err = np.array([])
    rhoyz_num_err  = np.array([])
    system = str(sys)
    if sys == 1:
        color = color1
        zorder = 1
        
    elif sys == 2:
        color = color2
        zorder = 9
        
    elif sys == 3:
        color = color6
        zorder = 10
        
    elif sys == 4:
        color = color1
        zorder = 1
        
    elif sys ==5:
        color = color1
        zorder = 1
        
    elif sys == 6:
        color = color4
        zorder = 7
        
    elif sys == 7:
        color = color3
        zorder = 10
        
    elif sys == 8:
        color = color5
        zorder = 10
    elif sys == 9:
        color = color1
        zorder = 1
    elif sys == 10:
        color = color4
        zorder = 7
    
    
    
    for vol in [1,2,3]:
        
        volume = str(vol)



        path = '../simulations/fig-2-simulations/v6/system_' + system + '/vol_dynamic_' + volume + '/results/'

        if sys == 10:
            number_of_splits = 4
        
        elif sys == 8 and vol == 1:
            number_of_splits = 3
            
        elif sys == 4 and vol == 2:
            number_of_splits = 4
        
        elif sys == 5 or sys == 6 or sys == 7:
            number_of_splits = 4
        
        else:
            number_of_splits = 5
        for i in range(number_of_splits):
            
            split_number = str(i+1)

        
        
            #etaxz conc
            name = 'split_'+split_number+' _s' + system + '_v' + volume + '_pearson_xz_numbers.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path + name, delimiter=',')
            if (data.ndim > 0):
                rhoxz_conc = np.concatenate([rhoxz_conc, data])
            
                name = 'split_'+split_number+' _s' + system + '_v' + volume + '_pearson_yz_numbers.csv'
                data = np.genfromtxt(path + name, delimiter=',')
                rhoyz_conc = np.concatenate([rhoyz_conc, data])
                                

        marker = '.' 
        markersizes = 1
        ax.scatter(rhoxz_conc, rhoyz_conc, marker = '.',  s = markersizes, color = color, zorder = zorder)


plt.ylim([-0.2,1])
plt.xlim([-0.2,1])



# set the x-spine
ax.spines['left'].set_position('zero')

# turn off the right spine/ticks
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

# set the y-spine
ax.spines['bottom'].set_position('zero')

# turn off the top spine/ticks
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()
plt.xlabel(r'Pearson correlation $\rho_{xz}$', fontsize = 10)
plt.ylabel(r'Pearson correlation $\rho_{xz}$', fontsize = 10)
plt.xticks([0,1], ['0.0', '1.0'], fontsize = 10)
plt.yticks([0,1], ['0.0', '1.0'], fontsize = 10)

plt.tight_layout()

