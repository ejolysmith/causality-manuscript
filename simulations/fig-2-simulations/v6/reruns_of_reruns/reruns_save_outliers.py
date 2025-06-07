
import numpy as np
import random
import math
import itertools

import multiprocessing

import uncertainties as un

from uncertainties import unumpy


N = 0

number_of_splits = 5 #system 10 split 5 is weird. 

for sys in [1,2,3,4,5,6,7,8,9,10]:  #4,5
    system = str(sys)
    for vol in [1,2,3]:
        
        
        etaxz_conc = np.array([])
        etaxz_num  = np.array([])
        etaxz_conc_err = np.array([])
        etaxz_num_err  = np.array([])
        etayz_conc = np.array([])
        etayz_num  = np.array([])
        etayz_conc_err = np.array([])
        etayz_num_err  = np.array([])
        beta_w = np.array([])
        beta_x = np.array([])
        beta_y = np.array([])
        beta_z = np.array([])
        lamda_w = np.array([])
        lamda_z = np.array([])
        lamda = np.array([])
        k = np.array([])
        A = np.array([])
        B = np.array([])
        C = np.array([])
        omega = np.array([])
        system_number = np.array([])
        volume_number = np.array([])
        number_of_simulations = np.array([])

        volume = str(vol)



        path = 'system_' + system + '/vol_dynamic_' + volume + '/results/bad_parameters/rerun/'



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

        
        #beta_w
        name = 'rerun_s' + system + '_v' + volume + '_beta_w.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        beta_w = np.append(beta_w, data)

        #beta_x
        name = 'rerun_s' + system + '_v' + volume + '_beta_x.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        beta_x = np.append(beta_x, data)
        
        #beta_y
        name = 'rerun_s' + system + '_v' + volume + '_beta_y.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        beta_y = np.append(beta_y, data)

        #beta_z
        name = 'rerun_s' + system + '_v' + volume + '_beta_z.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        beta_z = np.append(beta_z, data)

        #lamda_w
        name = 'rerun_s' + system + '_v' + volume + '_lamda_w.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        lamda_w = np.append(lamda_w, data)

        #lamda_z
        name = 'rerun_s' + system + '_v' + volume + '_lamda_z.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        lamda_z = np.append(lamda_z, data)
        

        #lamda
        name = 'rerun_s' + system + '_v' + volume + '_lamda.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        lamda = np.append(lamda, data)
        
        
        #k
        name = 'rerun_s' + system + '_v' + volume + '_k.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        k = np.append(k, data)
    
        #A (only exists in systems 6 and 10)
        if sys == 6 or sys == 10:
            name = 'rerun_s' + system + '_v' + volume + '_A.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path + name, delimiter=',')
            A = np.append(A, data)
        
        
        #B (only exists in systems 6 and 10)
        if sys == 6 or sys == 10:
            name = 'rerun_s' + system + '_v' + volume + '_B.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path + name, delimiter=',')
            B = np.append(B, data)
        

        #A (only exists in systems 6 and 10)
        if sys == 6 or sys == 10:
            name = 'rerun_s' + system + '_v' + volume + '_C.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path + name, delimiter=',')
            C = np.append(C, data)
        

        #omega (only exists in systems 6 and 10)
        if sys == 6 or sys == 10:
            name = 'rerun_s' + system + '_v' + volume + '_omega.csv'
            #np.genfromtxt('myfile.csv', delimiter=',')
            data = np.genfromtxt(path + name, delimiter=',')
            omega = np.append(omega, data)
        

        
        #number of simulations
        name = 'rerun_s' + system + '_v' + volume + '_number_of_simulations.csv'
        #np.genfromtxt('myfile.csv', delimiter=',')
        data = np.genfromtxt(path + name, delimiter=',')
        number_of_simulations = np.append(number_of_simulations, data)
        
        #volume number
        data = vol*np.ones(len(k))
        volume_number = np.append(volume_number, data)
        
        #system number
        data = sys*np.ones(len(k))
        system_number = np.append(system_number, data)








        etaxz_conc = unumpy.uarray(etaxz_conc, etaxz_conc_err)
        etayz_conc = unumpy.uarray(etayz_conc, etayz_conc_err)
        ratio_conc = etaxz_conc/etayz_conc
        
        etaxz_num = unumpy.uarray(etaxz_num, etaxz_num_err)
        etayz_num = unumpy.uarray(etayz_num, etayz_num_err)
        ratio_num = etaxz_num/etayz_num
        
        
        beta_w_conc_bad  = []
        beta_x_conc_bad  = []
        beta_y_conc_bad  = []
        beta_z_conc_bad  = []
        lamda_w_conc_bad = []
        lamda_z_conc_bad = []
        lamda_conc_bad   = []
        k_conc_bad       = []
        A_conc_bad       = []
        B_conc_bad       =[]
        C_conc_bad = []
        omega_conc_bad = []
        number_of_simulations_conc_bad = []
        system_number_conc_bad = []
        volume_number_conc_bad = []
        
        
        
        beta_w_num_bad  = []
        beta_x_num_bad  = []
        beta_y_num_bad  = []
        beta_z_num_bad  = []
        lamda_w_num_bad = []
        lamda_z_num_bad = []
        lamda_num_bad   = []
        k_num_bad       = []
        k_num_bad       = []
        A_num_bad       = []
        B_num_bad       =[]
        C_num_bad = []
        omega_num_bad = []
        number_of_simulations_num_bad = []
        system_number_num_bad = []
        volume_number_num_bad = []
        
        
        
        ratio_conc_bad   = []
        ratio_num_bad    = []
        
        
        
        
        for i in range(len(etaxz_conc)):
            if  etaxz_conc[i] != -501 and abs(ratio_conc[i].nominal_value - 1) > ratio_conc[i].std_dev:
                beta_w_conc_bad.append( beta_w[i] )
                beta_x_conc_bad.append( beta_x[i] )
                beta_y_conc_bad.append( beta_y[i] )
                beta_z_conc_bad.append( beta_z[i] )
                lamda_w_conc_bad.append( lamda_w[i] )
                lamda_z_conc_bad.append( lamda_z[i] )
                lamda_conc_bad.append( lamda[i] )
                k_conc_bad.append( k[i] )
                if sys == 6 or sys == 10:
                    A_conc_bad.append(A[i] )
                    B_conc_bad.append(B[i] )
                    C_conc_bad.append(C[i] )
                    omega_conc_bad.append(omega[i] )
                number_of_simulations_conc_bad.append(number_of_simulations[i] )
                
                
                ratio_conc_bad.append( ratio_conc[i].nominal_value)
                N = N + 1 
                
            #if  etaxz_conc[i] != -501 and abs(ratio_num[i].nominal_value - 1) > ratio_num[i].std_dev:
            #    beta_w_num_bad.append(beta_w[i)
            #    beta_x_num_bad.append( beta_x[i)
            #    beta_y_num_bad.append( beta_y[i)
            #    beta_z_num_bad.append( beta_z[i)
            #    lamda_w_num_bad.append( lamda_w[i)
            #    lamda_z_num_bad.append( lamda_z[i)
            #    lamda_num_bad.append( lamda[i)
            #    k_num_bad.append( k[i)
            #    ratio_num_bad.append( ratio_num[i)
            
            
        #number_of_good_simulations = 0
        #for i in range(len(etaxz_conc)):
        #    if etaxz_conc[i] != -501:
        #        number_of_good_simulations += 1
                
        #print(len(ratio_conc_bad)/number_of_good_simulations*100)
        
        
        
        
        save_path = 'system_' + system + '/vol_dynamic_' + volume + '/results/bad_parameters/rerun/bad_parameters/s' + system + '_v' + volume + '_bad_conc'
            
        #save_path = 's' + system + '_v' + volume + '_bad_conc'
        np.savetxt(save_path + '_lamda.csv', lamda_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_lamda_z.csv', lamda_z_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_lamda_w.csv', lamda_w_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_beta_x.csv', beta_x_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_beta_y.csv', beta_y_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_beta_z.csv', beta_z_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_beta_w.csv', beta_w_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_k.csv', k_conc_bad, delimiter = ',')
        
        if sys == 6 or sys == 10:
            np.savetxt(save_path + '_A.csv', A_conc_bad, delimiter = ',')
            np.savetxt(save_path + '_B.csv', B_conc_bad, delimiter = ',')
            np.savetxt(save_path + '_C.csv', C_conc_bad, delimiter = ',')
            np.savetxt(save_path + '_omega.csv', omega_conc_bad, delimiter = ',')
            
        np.savetxt(save_path + '_number_of_simulations.csv', number_of_simulations_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_ratio.csv', ratio_conc_bad, delimiter = ',')
        
        
        
        """
        save_path = 'results/bad_parameters/s' + system + '_v' + volume + '_bad_num'
        #save_path = 's' + system + '_v' + volume + '_bad_num'
        np.savetxt(save_path + '_lamda.csv', lamda_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_lamda_z.csv', lamda_z_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_lamda_w.csv', lamda_w_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_beta_x.csv', beta_x_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_beta_y.csv', beta_y_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_beta_z.csv', beta_z_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_beta_w.csv', beta_w_conc_bad, delimiter = ',')
        np.savetxt(save_path + '_k.csv', k_conc_bad, delimiter = ',')
        """
