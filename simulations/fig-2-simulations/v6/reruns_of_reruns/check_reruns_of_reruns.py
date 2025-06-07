import numpy as np

from uncertainties import unumpy






etaxz_conc = np.array([])
etaxz_num  = np.array([])
etaxz_conc_err = np.array([])
etaxz_num_err  = np.array([])
etayz_conc = np.array([])
etayz_num = np.array([])
etayz_conc_err = np.array([])
etayz_num_err  = np.array([])



number_of_simulations_rerun = []

for sys in [1,2,3,4,5,6,7,8,9,10]: 
    system = str(sys)
    for vol in [1,2,3]:

        volume = str(vol)



        path = 'system_' + system + '/vol_dynamic_' + volume + '/results/bad_parameters/rerun/bad_parameters/rerun/'




        
                
        
                

        #etaxz conc
        name = 'rerun_s' + system + '_v' + volume + '_eta_xz.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        etaxz_conc = np.append(etaxz_conc, data)
    
        
        #etayz conc
        name = 'rerun_s' + system + '_v' + volume + '_eta_yz.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        etayz_conc = np.append(etayz_conc, data)
        
        #etaxz num
        name = 'rerun_s' + system + '_v' + volume + '_eta_xz_numbers.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        etaxz_num = np.append(etaxz_num, data)
        
        #etayz num
        name = 'rerun_s' + system + '_v' + volume + '_eta_yz_numbers.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        etayz_num = np.append(etayz_num, data)
        
        
        
        #etaxz conc err
        name = 'rerun_s' + system + '_v' + volume + '_eta_xz_error.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        etaxz_conc_err = np.append(etaxz_conc_err, data)
        
        #etayz conc err
        name = 'rerun_s' + system + '_v' + volume + '_eta_yz_error.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        etayz_conc_err = np.append(etayz_conc_err, data)
        
        #etaxz num err
        name = 'rerun_s' + system + '_v' + volume + '_eta_xz_error_numbers.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        etaxz_num_err = np.append(etaxz_num_err, data)
        
        #etayz num err
        name = 'rerun_s' + system + '_v' + volume + '_eta_yz_error_numbers.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        etayz_num_err = np.append(etayz_num_err, data)





#etaxz_conc = unumpy.uarray(etaxz_conc, etaxz_conc_err)
#etayz_conc = unumpy.uarray(etayz_conc, etayz_conc_err)
#ratio_conc = etaxz_conc/etayz_conc

#etaxz_conc_rerun = unumpy.uarray(etaxz_conc_rerun, etaxz_conc_err_rerun)
#etayz_conc_rerun = unumpy.uarray(etayz_conc_rerun, etayz_conc_err_rerun)
ratio_conc_rerun = etaxz_conc/etayz_conc

etaxz_conc_rerun_un = unumpy.uarray(etaxz_conc, etaxz_conc_err)
etayz_conc_rerun_un = unumpy.uarray(etayz_conc, etayz_conc_err)
ratio_conc_rerun_un = etaxz_conc_rerun_un/etayz_conc_rerun_un



N = 0
for i in range(len(etaxz_conc_rerun_un)):
    if  abs(ratio_conc_rerun_un[i].nominal_value - 1) > ratio_conc_rerun_un[i].std_dev:
        #print("HEHE")
        #print(i)
        N = N + 1
        
        
print(N)

