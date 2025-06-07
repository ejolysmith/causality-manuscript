import numpy as np

from uncertainties import unumpy






etaxz_conc_rerun = np.array([])
etaxz_num_rerun  = np.array([])
etaxz_conc_err_rerun = np.array([])
etaxz_num_err_rerun  = np.array([])
etayz_conc_rerun = np.array([])
etayz_num_rerun  = np.array([])
etayz_conc_err_rerun = np.array([])
etayz_num_err_rerun  = np.array([])

ratio_conc_bad = np.array([])


number_of_simulations_rerun = []

number_of_splits = 5 #system 10 split 5 is weird. 
for sys in [1,2,3,4,5,6,7,8,9,10]:  #4,5
    system = str(sys)
    for vol in [1,2,3]:

        volume = str(vol)



        path = 'system_' + system + '/vol_dynamic_' + volume + '/results/bad_parameters/'
        path2 = 'system_' + system + '/vol_dynamic_' + volume + '/results/bad_parameters/rerun/'




        
        
        #etaxz conc
        name = 's' + system + '_v' + volume + '_bad_conc_ratio.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        if (data.ndim > 0):
            ratio_conc_bad = np.concatenate([ratio_conc_bad, data])
        else:
            ratio_conc_bad = np.append(ratio_conc_bad, data)
                
        
                

        #etaxz conc
        name = 'rerun_s' + system + '_v' + volume + '_eta_xz.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path2 + name, delimiter=',')
        if (data.ndim > 0):
            etaxz_conc_rerun = np.concatenate([etaxz_conc_rerun, data])
        
            
            #etayz conc
            name = 'rerun_s' + system + '_v' + volume + '_eta_yz.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path2 + name, delimiter=',')
            etayz_conc_rerun = np.concatenate([etayz_conc_rerun, data])
            
            #etaxz conc err
            name = 'rerun_s'  + system + '_v' + volume + '_eta_xz_error.csv'
            #np.genfromtxt(path2 + name, delimiter=',')
            data = np.genfromtxt(path2 + name, delimiter=',')
            etaxz_conc_err_rerun = np.concatenate([etaxz_conc_err_rerun, data])
            
            #etayz conc err
            name = 'rerun_s'  + system + '_v' + volume + '_eta_yz_error.csv'
            #np.genfromtxt(path2 + name, delimiter=',')
            data = np.genfromtxt(path2 + name, delimiter=',')
            etayz_conc_err_rerun = np.concatenate([etayz_conc_err_rerun, data])
            
            
            name = 'rerun_s'  + system + '_v' + volume + '_number_of_simulations.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path2 + name, delimiter=',')
            number_of_simulations_rerun = np.concatenate([number_of_simulations_rerun, data])
            
        else:
            etaxz_conc_rerun = np.append(etaxz_conc_rerun, data)
            #etayz conc
            name = 'rerun_s'  + system + '_v' + volume + '_eta_yz.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path2 + name, delimiter=',')
            etayz_conc_rerun = np.append(etayz_conc_rerun, data)
            
            #etaxz conc err
            name = 'rerun_s'  + system + '_v' + volume + '_eta_xz_error.csv'
            #np.genfromtxt(path2 + name, delimiter=',')
            data = np.genfromtxt(path2 + name, delimiter=',')
            etaxz_conc_err_rerun = np.append(etaxz_conc_err_rerun, data)
            
            #etayz conc err
            name = 'rerun_s'  + system + '_v' + volume + '_eta_yz_error.csv'
            #np.genfromtxt(path2 + name, delimiter=',')
            data = np.genfromtxt(path2 + name, delimiter=',')
            etayz_conc_err_rerun = np.append(etayz_conc_err_rerun, data)
            
            
            name = 'rerun_s'  + system + '_v' + volume + '_number_of_simulations.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path2 + name, delimiter=',')
            number_of_simulations_rerun = np.append(number_of_simulations_rerun, data)





#etaxz_conc = unumpy.uarray(etaxz_conc, etaxz_conc_err)
#etayz_conc = unumpy.uarray(etayz_conc, etayz_conc_err)
#ratio_conc = etaxz_conc/etayz_conc

#etaxz_conc_rerun = unumpy.uarray(etaxz_conc_rerun, etaxz_conc_err_rerun)
#etayz_conc_rerun = unumpy.uarray(etayz_conc_rerun, etayz_conc_err_rerun)
ratio_conc_rerun = etaxz_conc_rerun/etayz_conc_rerun

etaxz_conc_rerun_un = unumpy.uarray(etaxz_conc_rerun, etaxz_conc_err_rerun)
etayz_conc_rerun_un = unumpy.uarray(etayz_conc_rerun, etayz_conc_err_rerun)
ratio_conc_rerun_un = etaxz_conc_rerun_un/etayz_conc_rerun_un



N = 0
for i in range(len(etaxz_conc_rerun_un)):
    if  abs(ratio_conc_rerun_un[i].nominal_value - 1) > ratio_conc_rerun_un[i].std_dev:
        #print("HEHE")
        #print(i)
        N = N + 1
        
        
print(N/len(ratio_conc_bad)*100)

