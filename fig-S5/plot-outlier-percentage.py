import numpy as np
from matplotlib import pylab as plt
from uncertainties import unumpy
number_of_splits = 5




percentages = np.zeros(10)
numbers = np.zeros(10)
errors = np.zeros(10)
distances = np.zeros(10)



for sys in [1,2,3,4,5,6,7,8,9,10]: 

    etaxz_conc = np.array([])
    etaxz_num  = np.array([])
    etaxz_conc_err = np.array([])
    etaxz_num_err  = np.array([])
    etayz_conc = np.array([])
    etayz_num  = np.array([])
    etayz_conc_err = np.array([])
    etayz_num_err  = np.array([])
    system = str(sys)
    
    
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
            name = 'split_'+split_number+' _s' + system + '_v' + volume + '_eta_xz.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path + name, delimiter=',')
            if (data.ndim > 0):
                etaxz_conc = np.concatenate([etaxz_conc, data])
            
                
                #etayz conc
                name = 'split_'+split_number+' _s' + system + '_v' + volume + '_eta_yz.csv'
                #np.genfromtxt('myfile.csv', delimiter=',')
                data = np.genfromtxt(path + name, delimiter=',')
                etayz_conc = np.concatenate([etayz_conc, data])
                
                #etaxz num
                name = 'split_'+split_number+' _s' + system + '_v' + volume + '_eta_xz_numbers.csv'
                #np.genfromtxt('myfile.csv', delimiter=',')
                data = np.genfromtxt(path + name, delimiter=',')
                etaxz_num = np.concatenate([etaxz_num, data])
                
                #etayz num
                name = 'split_'+split_number+' _s' + system + '_v' + volume + '_eta_yz_numbers.csv'
                #np.genfromtxt('myfile.csv', delimiter=',')
                data = np.genfromtxt(path + name, delimiter=',')
                etayz_num = np.concatenate([etayz_num, data])
                
                
                
                
                #etaxz conc err
                name = 'split_'+split_number+' _s' + system + '_v' + volume + '_eta_xz_error.csv'
                #np.genfromtxt('myfile.csv', delimiter=',')
                data = np.genfromtxt(path + name, delimiter=',')
                etaxz_conc_err = np.concatenate([etaxz_conc_err, data])
                
                #etayz conc err
                name = 'split_'+split_number+' _s' + system + '_v' + volume + '_eta_yz_error.csv'
                #np.genfromtxt('myfile.csv', delimiter=',')
                data = np.genfromtxt(path + name, delimiter=',')
                etayz_conc_err = np.concatenate([etayz_conc_err, data])
                
                #etaxz num err
                name = 'split_'+split_number+' _s' + system + '_v' + volume + '_eta_xz_error_numbers.csv'
                #np.genfromtxt('myfile.csv', delimiter=',')
                data = np.genfromtxt(path + name, delimiter=',')
                etaxz_num_err = np.concatenate([etaxz_num_err, data])
                
                #etayz num err
                name = 'split_'+split_number+' _s' + system + '_v' + volume + '_eta_yz_error_numbers.csv'
                #np.genfromtxt('myfile.csv', delimiter=',')
                data = np.genfromtxt(path + name, delimiter=',')
                etayz_num_err = np.concatenate([etayz_num_err, data])
        
                
        
        max_err = np.zeros(len(etaxz_conc_err))
        for i in range(len(max_err)):
            max_err[i] = max([etaxz_conc_err[i], etayz_conc_err[i]])





        eta_err = np.zeros(len(etaxz_conc_err) + len(etayz_conc_err))
        eta_err[:len(etaxz_conc_err)] = etaxz_conc_err/np.abs(etaxz_conc)
        eta_err[len(etaxz_conc_err):] = etayz_conc_err/np.abs(etayz_conc)
        

        dist = np.abs(etaxz_conc - etayz_conc)/np.sqrt(2)/np.abs(etaxz_conc*0.5 + etayz_conc*0.5)*100
        #average_dist = np.average(dist)

        etaxz_conc_u = unumpy.uarray(etaxz_conc, etaxz_conc_err)
        etayz_conc_u = unumpy.uarray(etayz_conc, etayz_conc_err)
        ratio_conc = etaxz_conc_u/etayz_conc_u
        ratio_conc_val = np.zeros(len(ratio_conc))
        ratio_conc_err = np.zeros(len(ratio_conc))
        for lll in range(len(ratio_conc)):
            ratio_conc_val[lll] = ratio_conc[lll].nominal_value
            ratio_conc_err[lll] = ratio_conc[lll].std_dev

        etaxz_num_u = unumpy.uarray(etaxz_num, etaxz_num_err)
        etayz_num_u = unumpy.uarray(etayz_num, etayz_num_err)
        ratio_num = etaxz_num/etayz_num

        sys_indices = np.array(range(len(etaxz_conc)))
        
        n = 0
        m = 0
        per = 0
        average_err = 0
        average_dist = 0
        for oo in range(len(ratio_conc)):
            if etaxz_conc[oo] != -501:
                n = n + 1
                average_dist = average_dist + dist[oo]
                if abs(ratio_conc[oo].nominal_value - 1) > ratio_conc[oo].std_dev:
                    per = per + 1
                    
        for oo in range(len(etaxz_conc)):
            if etaxz_conc[oo] != -501:
                m = m + 1
                average_err = average_err + etaxz_conc_err[oo]#/np.abs(etaxz_conc[oo])*100
        for oo in range(len(etayz_conc)):
            if etaxz_conc[oo] != -501:
                m = m + 1
                average_err = average_err + etayz_conc_err[oo]#/np.abs(etayz_conc[oo])*100
                
        
        percentages[sys-1] = per/n*100
        numbers[sys-1] = n
        errors[sys-1] = average_err/m
        distances[sys-1] = average_dist/n
        
        marker = '.' 



xplot = np.array(range(10)) + 1

fig1, ax1 = plt.subplots(figsize = (2.5,2.5))
ax1.plot(xplot, percentages, '.')

plt.ylim([0,50])
plt.xlim([0,11])
plt.xticks([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10], fontsize = 10)
plt.ylabel(r'Outlier percentage', fontsize = 10)
plt.xlabel(r'Process index', fontsize = 10)
plt.tight_layout()


fig2, ax2 = plt.subplots(figsize = (2.5,2.5))
ax2.plot(xplot, numbers, '.')

plt.xticks([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10], fontsize = 10)
plt.ylabel(r'Number of simulated' + '\n' 'parameters sets', fontsize = 10)
plt.xlabel(r'Process index', fontsize = 10)
plt.tight_layout()
