#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:36:05 2023

@author: mikdad
"""

import numpy as np
import random
import math
import itertools
import sys
import multiprocessing


number_of_cores = int(sys.argv[1])   
system_number = '9'  #first argument after .py file is number of cores
volume_number = '2'
split_number = sys.argv[2]

import time as timer
start = timer.perf_counter()

import os 

#scratch_dir  = os.environ['SCRATCH']
path_2 = '/scratch/smitheua/v6'
sys.path.append(path_2)
import new_vol_dyn
#import pandas as pd


global_jump_time_factor = 20000 #Number of divisions
number_of_parameters = 1000
min_err = 0.01



def read_file(x):
    y = np.genfromtxt(x, delimiter=',').flatten()
    #y = (np.array(pd.read_csv(x))).flatten()
    return y


bad_parameter_path = path_2 + '/system_' + system_number + '/vol_dynamic_' +\
    volume_number + '/results/bad_parameters/s' + system_number + '_v' + volume_number + '_bad_'



jump_time_1_factor = global_jump_time_factor


jump_times = list(np.arange(1, jump_time_1_factor, 1))
    #list(np.linspace(1, jump_time_1_factor , jump_time_1_factor))

stay_prob = np.ones(len(jump_times) -1 )
stay_prob[:] = 0.5
   # stay_prob[0: -1 : 2] = 0.6
stay_prob = list(stay_prob)



def s5_v1_covariance(inputs2):
    lamda = inputs2[0]
    lamda_z = inputs2[1]
    lamda_w = inputs2[2]
    eta_x  = inputs2[3]
    beta_y = inputs2[4]
    beta_x = beta_y
    beta_z = inputs2[5]
    beta_w = inputs2[6]
    k = inputs2[7]
    V0 = inputs2[8]
    Vmax = inputs2[9]
    a = inputs2[10]
    #jump_times = inputs2[11]
    #stay_prob = inputs2[12]
    w_initial = inputs2[13]
    x_initial = inputs2[14]
    y_initial = inputs2[15]
    z_initial = inputs2[16]
    endtime = inputs2[17]

    
    
    #n = 3 #Assymetric feedback with cofounding variable had an n dependance
    
    #System 6 upstream temporal signal parameters
    A = 1
    B = 1.2
    C = 1.4
    omega = 1.5
    
    
    x = int(x_initial)
    y = int(y_initial)
    z = int(z_initial)
    w = int(w_initial)

    shadow = 0
    
    time = 0
    waittimes = 0
    interval_time = 0 
    
    T = 0 #Counter for jump_times
    
    volume = new_vol_dyn.lin_V(V0, interval_time)
    
    #--------------
    #Setting as 0 for now will add in conc later
    eta_xz_conc = 0
    eta_yz_conc = 0
    pearson_xz_conc = 0
    pearson_yz_conc = 0
    
    
    #------------
    #Initializing variablesa for running averages of concentrations
    
    
    #--------------------------------------------------------------------
    #Initialzing variables and variables for running average of abundances
    
    xz = x * z
    yz = y * z 
    
    x_sq = x ** 2
    y_sq = y ** 2
    z_sq = z ** 2
    
    ith_x_avg = 0
    ith_y_avg = 0
    ith_z_avg = 0
    
    ith_xz_avg = 0
    ith_yz_avg = 0
    
    ith_x_sq_avg = 0
    ith_y_sq_avg = 0
    ith_z_sq_avg = 0
    
    
    #--------------------------------------------------------------------
    
    #------------
    #Initializing variablesa for running averages of concentrations
    
    ith_conc_x_avg = 0
    ith_conc_y_avg = 0
    ith_conc_z_avg = 0
    
    ith_xz_v2_avg = 0
    ith_yz_v2_avg = 0
    
    
    ith_x_sq_v2_avg = 0
    ith_y_sq_v2_avg = 0
    ith_z_sq_v2_avg = 0
    
    #-------------------------------
    
    
    while time < endtime/100:
        
        if T < len(jump_times) - 1 : #If we have some jumps remaining
                    
            
            x_birth_rate = 2*lamda * z / (k + x)
            x_death_rate = z * x
            
            y_birth_rate = lamda * z / (k + x)
            y_death_rate = z * y
            
            z_birth_rate = lamda_z
            z_death_rate = beta_z * z
            
            w_birth_rate = 0 #System 5 has no w
            w_death_rate = 0

            
            
            maximal_rate = 0   #Set with the assumption that volume at most
                                                                    #doubles (ensured by parameteres of cell divison)
            
            shadow_birth_rate = 0

            r_t = x_birth_rate + x_death_rate + y_birth_rate + y_death_rate + shadow_birth_rate + z_birth_rate + z_death_rate + w_birth_rate + w_death_rate
    
            
            
            u_time = random.uniform(0, 1)
            t = - (math.log(u_time)) / r_t
            
            #u_event = random.uniform(0,1)
            
            
            if time + t < jump_times[T]:
                
                time += t
                waittimes = t
                
                interval_time += t
                
# =============================================================================
#                 ith_x_avg = new_vol_dyn.running_abundance_avg(x, ith_x_avg, waittimes, time)
#                 ith_y_avg = new_vol_dyn.running_abundance_avg(y, ith_y_avg, waittimes, time)
#                 ith_z_avg = new_vol_dyn.running_abundance_avg(z, ith_z_avg, waittimes, time)
#                 
#                 ith_xz_avg = new_vol_dyn.running_abundance_avg(xz, ith_xz_avg, waittimes, time)
#                 ith_yz_avg = new_vol_dyn.running_abundance_avg(yz, ith_yz_avg, waittimes, time)
#                 
#                 ith_x_sq_avg = new_vol_dyn.running_abundance_avg(x_sq, ith_x_sq_avg, waittimes, time)
#                 ith_y_sq_avg = new_vol_dyn.running_abundance_avg(y_sq, ith_y_sq_avg, waittimes, time)
#                 ith_z_sq_avg = new_vol_dyn.running_abundance_avg(z_sq, ith_z_sq_avg, waittimes, time)
# =============================================================================
                
                volume = new_vol_dyn.lin_V(V0, interval_time)
                
                x_birth_rate = 2*lamda * z / (k + x)
                x_death_rate = z * x
            
                y_birth_rate = lamda * z / (k + x)
                y_death_rate = z * y
            
                z_birth_rate = lamda_z
                z_death_rate = beta_z * z
            
                w_birth_rate = 0 #System 5 has no w
                w_death_rate = 0


                u_event = random.uniform(0,1)
                
                #r_t vol indep so its the same as the one computed above before volume was updated
                
                x_birth_prob = x_birth_rate / r_t
                x_death_prob = (x_birth_rate + x_death_rate) / r_t
                
                y_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate) /r_t
                y_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate) /r_t
                
                z_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate + z_birth_rate) /r_t
                z_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                                + z_birth_rate + z_death_rate) /r_t
                    
                w_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                                + z_birth_rate + z_death_rate + w_birth_rate) /r_t
                
                w_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                                + z_birth_rate + z_death_rate + w_birth_rate + w_death_rate) /r_t
                    
                if u_event < x_birth_prob:
                    x += 1
                 
        
                elif u_event < x_death_prob:
                    x += -1
                    
                   
                elif u_event < y_birth_prob:
                    y += 1
                    
                elif u_event < y_death_prob:
                    y += -1
                    
                    
                elif u_event < z_birth_prob:
                    
                    z += 1
                    
                    
                elif u_event < z_death_prob:
                  
                    z += -1
                
                elif u_event < w_birth_prob:
                    
                    w += 1
                    
                elif u_event < w_death_prob:
                    
                    w += -1
                
                    
                    
                xz = x * z
                yz = y * z 
                
                x_sq = x ** 2
                y_sq = y ** 2
                z_sq = z ** 2
            
            
            elif time + t >= jump_times[T]: #Jump T happens
            
                interval_time += jump_times[T] - time
                waittimes = (jump_times[T] - time)
                time = jump_times[T]
                
# =============================================================================
#                 ith_x_avg = new_vol_dyn.running_abundance_avg(x, ith_x_avg, waittimes, time)
#                 ith_y_avg = new_vol_dyn.running_abundance_avg(y, ith_y_avg, waittimes, time)
#                 ith_z_avg = new_vol_dyn.running_abundance_avg(z, ith_z_avg, waittimes, time)
#                 
#                 ith_xz_avg = new_vol_dyn.running_abundance_avg(xz, ith_xz_avg, waittimes, time)
#                 ith_yz_avg = new_vol_dyn.running_abundance_avg(yz, ith_yz_avg, waittimes, time)
#                 
#                 ith_x_sq_avg = new_vol_dyn.running_abundance_avg(x_sq, ith_x_sq_avg, waittimes, time)
#                 ith_y_sq_avg = new_vol_dyn.running_abundance_avg(y_sq, ith_y_sq_avg, waittimes, time)
#                 ith_z_sq_avg = new_vol_dyn.running_abundance_avg(z_sq, ith_z_sq_avg, waittimes, time)
# =============================================================================
                
                temp_vol = new_vol_dyn.lin_V(V0 ,  interval_time) * stay_prob[T]
                V0 = temp_vol
                interval_time = 0
                volume = (new_vol_dyn.lin_V(V0, interval_time))
                
                T += 1
                
                x_dec_matrix = np.random.uniform(size = x)
                prob_x = (x_dec_matrix < stay_prob[T - 1]).astype(int) #First time jump happens
                prob_x = prob_x - 1
                x_removed = np.sum(prob_x)
                x =  (x + x_removed)
                
                y_dec_matrix = np.random.uniform(size = y)
                prob_y = (y_dec_matrix < stay_prob[T - 1]).astype(int) #First time jump happens
                prob_y = prob_y - 1
                y_removed = np.sum(prob_y)
                y = ( (y + y_removed))
                
                z_dec_matrix = np.random.uniform(size = z)
                prob_z = (z_dec_matrix < stay_prob[T - 1]).astype(int) #First time jump happens
                prob_z = prob_z - 1
                z_removed = np.sum(prob_z)
                z = ( (z + z_removed))
                
                w_dec_matrix = np.random.uniform(size = w)
                prob_w = (w_dec_matrix < stay_prob[T - 1]).astype(int) #First time jump happens
                prob_w = prob_w - 1
                w_removed = np.sum(prob_w)
                w = ( (w + w_removed))
                
                xz = x * z
                yz = y * z 
                
                x_sq = x ** 2
                y_sq = y ** 2
                z_sq = z ** 2
            
        else:
            x_birth_rate = 2*lamda * z / (k + x)
            x_death_rate = z * x
            
            y_birth_rate = lamda * z / (k + x)
            y_death_rate = z * y
            
            z_birth_rate = lamda_z
            z_death_rate = beta_z * z
            
            w_birth_rate = 0 #System 5 has no w
            w_death_rate = 0

            
            
            maximal_rate = 0   #Set with the assumption that volume at most
                                                                    #doubles (ensured by parameteres of cell divison)
            
            shadow_birth_rate = 0

            r_t = x_birth_rate + x_death_rate + y_birth_rate + y_death_rate + shadow_birth_rate + z_birth_rate + z_death_rate + w_birth_rate + w_death_rate
    
            
            
            u_time = random.uniform(0, 1)
            t = - (math.log(u_time)) / r_t
            
            time += t
            waittimes = t
            
            interval_time += t
            
# =============================================================================
#             ith_x_avg = new_vol_dyn.running_abundance_avg(x, ith_x_avg, waittimes, time)
#             ith_y_avg = new_vol_dyn.running_abundance_avg(y, ith_y_avg, waittimes, time)
#             ith_z_avg = new_vol_dyn.running_abundance_avg(z, ith_z_avg, waittimes, time)
#             
#             ith_xz_avg = new_vol_dyn.running_abundance_avg(xz, ith_xz_avg, waittimes, time)
#             ith_yz_avg = new_vol_dyn.running_abundance_avg(yz, ith_yz_avg, waittimes, time)
#             
#             ith_x_sq_avg = new_vol_dyn.running_abundance_avg(x_sq, ith_x_sq_avg, waittimes, time)
#             ith_y_sq_avg = new_vol_dyn.running_abundance_avg(y_sq, ith_y_sq_avg, waittimes, time)
#             ith_z_sq_avg = new_vol_dyn.running_abundance_avg(z_sq, ith_z_sq_avg, waittimes, time)
# =============================================================================
            
            volume = new_vol_dyn.lin_V(V0, interval_time)
            
            x_birth_rate = 2*lamda * z / (k + x)
            x_death_rate = z * x
            
            y_birth_rate = lamda * z / (k + x)
            y_death_rate = z * y
            
            z_birth_rate = lamda_z
            z_death_rate = beta_z * z
            
            w_birth_rate = 0 #System 5 has no w
            w_death_rate = 0

            
            u_event = random.uniform(0,1)
            
            #r_t vol indep so its the same as the one computed above before volume was updated
            
            x_birth_prob = x_birth_rate / r_t
            x_death_prob = (x_birth_rate + x_death_rate) / r_t
            
            y_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate) /r_t
            y_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate) /r_t
            
            z_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate + z_birth_rate) /r_t
            z_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                            + z_birth_rate + z_death_rate) /r_t
                
            w_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                            + z_birth_rate + z_death_rate + w_birth_rate) /r_t
            
            w_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                            + z_birth_rate + z_death_rate + w_birth_rate + w_death_rate) /r_t
                
            if u_event < x_birth_prob:
                x += 1
             
    
            elif u_event < x_death_prob:
                x += -1
                
               
            elif u_event < y_birth_prob:
                y += 1
                
            elif u_event < y_death_prob:
                y += -1
                
                
            elif u_event < z_birth_prob:
                
                z += 1
                
                
            elif u_event < z_death_prob:
              
                z += -1
            
            elif u_event < w_birth_prob:
                
                w += 1
                
            elif u_event < w_death_prob:
                
                w += -1
            
                
                
            xz = x * z
            yz = y * z 
            
            x_sq = x ** 2
            y_sq = y ** 2
            z_sq = z ** 2
    
    
    time = 0
    T = 0
    
    
    while time < endtime:
        
        if T < len(jump_times) - 1 : #If we have some jumps remaining
                    
            
            x_birth_rate = 2*lamda * z / (k + x)
            x_death_rate = z * x
            
            y_birth_rate = lamda * z / (k + x)
            y_death_rate = z * y
            
            z_birth_rate = lamda_z
            z_death_rate = beta_z * z
            
            w_birth_rate = 0 #System 5 has no w
            w_death_rate = 0

            
            
            maximal_rate = 0   #Set with the assumption that volume at most
                                                                    #doubles (ensured by parameteres of cell divison)
            
            shadow_birth_rate = 0

            r_t = x_birth_rate + x_death_rate + y_birth_rate + y_death_rate + shadow_birth_rate + z_birth_rate + z_death_rate + w_birth_rate + w_death_rate
    
            
            
            u_time = random.uniform(0, 1)
            t = - (math.log(u_time)) / r_t
            
            #u_event = random.uniform(0,1)
            
            
            if time + t < jump_times[T]:
                
                time += t
                waittimes = t
                
                interval_time += t
                
                volume = new_vol_dyn.lin_V(V0, interval_time)
                
                #-----------------------------------------------
                #Abundance averages
                
                ith_x_avg = new_vol_dyn.running_abundance_avg(x, ith_x_avg, waittimes, time)
                ith_y_avg = new_vol_dyn.running_abundance_avg(y, ith_y_avg, waittimes, time)
                ith_z_avg = new_vol_dyn.running_abundance_avg(z, ith_z_avg, waittimes, time)
                
                ith_xz_avg = new_vol_dyn.running_abundance_avg(xz, ith_xz_avg, waittimes, time)
                ith_yz_avg = new_vol_dyn.running_abundance_avg(yz, ith_yz_avg, waittimes, time)
                
                ith_x_sq_avg = new_vol_dyn.running_abundance_avg(x_sq, ith_x_sq_avg, waittimes, time)
                ith_y_sq_avg = new_vol_dyn.running_abundance_avg(y_sq, ith_y_sq_avg, waittimes, time)
                ith_z_sq_avg = new_vol_dyn.running_abundance_avg(z_sq, ith_z_sq_avg, waittimes, time)
                
                #----------------------------------------------------------
                
                #-----------------------------------------
                #Conc averages
                
                temp_conc_x_average = x * new_vol_dyn.temp_lin_one_over_vol_average(V0, waittimes, interval_time) / waittimes
                ith_conc_x_avg = new_vol_dyn.running_abundance_avg(temp_conc_x_average, ith_conc_x_avg, waittimes, time)
                
                temp_conc_y_average = y * new_vol_dyn.temp_lin_one_over_vol_average(V0, waittimes, interval_time) / waittimes
                ith_conc_y_avg = new_vol_dyn.running_abundance_avg(temp_conc_y_average, ith_conc_y_avg, waittimes, time)
                
                temp_conc_z_average = z * new_vol_dyn.temp_lin_one_over_vol_average(V0, waittimes, interval_time)/ waittimes
                ith_conc_z_avg = new_vol_dyn.running_abundance_avg(temp_conc_z_average, ith_conc_z_avg, waittimes, time)
                
                temp_xz_average = x * z * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_xz_v2_avg = new_vol_dyn.running_abundance_avg(temp_xz_average, ith_xz_v2_avg, waittimes, time)
                
                temp_yz_average = y * z * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_yz_v2_avg = new_vol_dyn.running_abundance_avg(temp_yz_average, ith_yz_v2_avg, waittimes, time)
                
                temp_x_sq_average = x *x * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_x_sq_v2_avg = new_vol_dyn.running_abundance_avg(temp_x_sq_average, ith_x_sq_v2_avg, waittimes, time)
                
                temp_y_sq_average = y *y * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_y_sq_v2_avg = new_vol_dyn.running_abundance_avg(temp_y_sq_average, ith_y_sq_v2_avg, waittimes, time)
                
                temp_z_sq_average = z *z * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_z_sq_v2_avg = new_vol_dyn.running_abundance_avg(temp_z_sq_average, ith_z_sq_v2_avg, waittimes, time)
                
                
                
                
                
                
                #----------------------------------------
                
                
                
                
                
                x_birth_rate = 2*lamda * z / (k + x)
                x_death_rate = z * x
            
                y_birth_rate = lamda * z / (k + x)
                y_death_rate = z * y
            
                z_birth_rate = lamda_z
                z_death_rate = beta_z * z
            
                w_birth_rate = 0 #System 5 has no w
                w_death_rate = 0



                u_event = random.uniform(0,1)
                
                #r_t vol indep so its the same as the one computed above before volume was updated
                
                x_birth_prob = x_birth_rate / r_t
                x_death_prob = (x_birth_rate + x_death_rate) / r_t
                
                y_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate) /r_t
                y_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate) /r_t
                
                z_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate + z_birth_rate) /r_t
                z_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                                + z_birth_rate + z_death_rate) /r_t
                    
                w_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                                + z_birth_rate + z_death_rate + w_birth_rate) /r_t
                
                w_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                                + z_birth_rate + z_death_rate + w_birth_rate + w_death_rate) /r_t
                    
                if u_event < x_birth_prob:
                    x += 1
                 
        
                elif u_event < x_death_prob:
                    x += -1
                    
                   
                elif u_event < y_birth_prob:
                    y += 1
                    
                elif u_event < y_death_prob:
                    y += -1
                    
                    
                elif u_event < z_birth_prob:
                    
                    z += 1
                    
                    
                elif u_event < z_death_prob:
                  
                    z += -1
                
                elif u_event < w_birth_prob:
                    
                    w += 1
                    
                elif u_event < w_death_prob:
                    
                    w += -1
                
                    
                    
                xz = x * z
                yz = y * z 
                
                x_sq = x ** 2
                y_sq = y ** 2
                z_sq = z ** 2
            
            
            elif time + t >= jump_times[T]: #Jump T happens
            
                interval_time += jump_times[T] - time
                waittimes = (jump_times[T] - time)
                time = jump_times[T]
                
                
                
                #-----------------------------------------------
                #Abundance averages
                
                ith_x_avg = new_vol_dyn.running_abundance_avg(x, ith_x_avg, waittimes, time)
                ith_y_avg = new_vol_dyn.running_abundance_avg(y, ith_y_avg, waittimes, time)
                ith_z_avg = new_vol_dyn.running_abundance_avg(z, ith_z_avg, waittimes, time)
                
                ith_xz_avg = new_vol_dyn.running_abundance_avg(xz, ith_xz_avg, waittimes, time)
                ith_yz_avg = new_vol_dyn.running_abundance_avg(yz, ith_yz_avg, waittimes, time)
                
                ith_x_sq_avg = new_vol_dyn.running_abundance_avg(x_sq, ith_x_sq_avg, waittimes, time)
                ith_y_sq_avg = new_vol_dyn.running_abundance_avg(y_sq, ith_y_sq_avg, waittimes, time)
                ith_z_sq_avg = new_vol_dyn.running_abundance_avg(z_sq, ith_z_sq_avg, waittimes, time)
                
                #----------------------------------------------------------
                
                #-----------------------------------------
                #Conc averages
                
                temp_conc_x_average = x * new_vol_dyn.temp_lin_one_over_vol_average(V0, waittimes, interval_time) / waittimes
                ith_conc_x_avg = new_vol_dyn.running_abundance_avg(temp_conc_x_average, ith_conc_x_avg, waittimes, time)
                
                temp_conc_y_average = y * new_vol_dyn.temp_lin_one_over_vol_average(V0, waittimes, interval_time) / waittimes
                ith_conc_y_avg = new_vol_dyn.running_abundance_avg(temp_conc_y_average, ith_conc_y_avg, waittimes, time)
                
                temp_conc_z_average = z * new_vol_dyn.temp_lin_one_over_vol_average(V0, waittimes, interval_time)/ waittimes
                ith_conc_z_avg = new_vol_dyn.running_abundance_avg(temp_conc_z_average, ith_conc_z_avg, waittimes, time)
                
                temp_xz_average = x * z * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_xz_v2_avg = new_vol_dyn.running_abundance_avg(temp_xz_average, ith_xz_v2_avg, waittimes, time)
                
                temp_yz_average = y * z * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_yz_v2_avg = new_vol_dyn.running_abundance_avg(temp_yz_average, ith_yz_v2_avg, waittimes, time)
                
                temp_x_sq_average = x *x * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_x_sq_v2_avg = new_vol_dyn.running_abundance_avg(temp_x_sq_average, ith_x_sq_v2_avg, waittimes, time)
                
                temp_y_sq_average = y *y * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_y_sq_v2_avg = new_vol_dyn.running_abundance_avg(temp_y_sq_average, ith_y_sq_v2_avg, waittimes, time)
                
                temp_z_sq_average = z *z * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
                ith_z_sq_v2_avg = new_vol_dyn.running_abundance_avg(temp_z_sq_average, ith_z_sq_v2_avg, waittimes, time)
                
                
                
                
                
                
                #----------------------------------------
                
                temp_vol = new_vol_dyn.lin_V(V0 ,  interval_time) * stay_prob[T]
                V0 = temp_vol
                interval_time = 0
                volume = (new_vol_dyn.lin_V(V0, interval_time))
                
                
                T += 1
                
                x_dec_matrix = np.random.uniform(size = x)
                prob_x = (x_dec_matrix < stay_prob[T - 1]).astype(int) #First time jump happens
                prob_x = prob_x - 1
                x_removed = np.sum(prob_x)
                x =  (x + x_removed)
                
                y_dec_matrix = np.random.uniform(size = y)
                prob_y = (y_dec_matrix < stay_prob[T - 1]).astype(int) #First time jump happens
                prob_y = prob_y - 1
                y_removed = np.sum(prob_y)
                y = ( (y + y_removed))
                
                z_dec_matrix = np.random.uniform(size = z)
                prob_z = (z_dec_matrix < stay_prob[T - 1]).astype(int) #First time jump happens
                prob_z = prob_z - 1
                z_removed = np.sum(prob_z)
                z = ( (z + z_removed))
                
                w_dec_matrix = np.random.uniform(size = w)
                prob_w = (w_dec_matrix < stay_prob[T - 1]).astype(int) #First time jump happens
                prob_w = prob_w - 1
                w_removed = np.sum(prob_w)
                w = ( (w + w_removed))
                
                xz = x * z
                yz = y * z 
                
                x_sq = x ** 2
                y_sq = y ** 2
                z_sq = z ** 2
            
        else:
            x_birth_rate = 2*lamda * z / (k + x)
            x_death_rate = z * x
            
            y_birth_rate = lamda * z / (k + x)
            y_death_rate = z * y
            
            z_birth_rate = lamda_z
            z_death_rate = beta_z * z
            
            w_birth_rate = 0 #System 5 has no w
            w_death_rate = 0

            
            
            maximal_rate = 0   #Set with the assumption that volume at most
                                                                    #doubles (ensured by parameteres of cell divison)
            
            shadow_birth_rate = 0

            r_t = x_birth_rate + x_death_rate + y_birth_rate + y_death_rate + shadow_birth_rate + z_birth_rate + z_death_rate + w_birth_rate + w_death_rate
    
            
            
            u_time = random.uniform(0, 1)
            t = - (math.log(u_time)) / r_t
            
            time += t
            waittimes = t
            
            interval_time += t
            
            volume = new_vol_dyn.lin_V(V0, interval_time)
            
            #-----------------------------------------------
            #Abundance averages
            
            ith_x_avg = new_vol_dyn.running_abundance_avg(x, ith_x_avg, waittimes, time)
            ith_y_avg = new_vol_dyn.running_abundance_avg(y, ith_y_avg, waittimes, time)
            ith_z_avg = new_vol_dyn.running_abundance_avg(z, ith_z_avg, waittimes, time)
            
            ith_xz_avg = new_vol_dyn.running_abundance_avg(xz, ith_xz_avg, waittimes, time)
            ith_yz_avg = new_vol_dyn.running_abundance_avg(yz, ith_yz_avg, waittimes, time)
            
            ith_x_sq_avg = new_vol_dyn.running_abundance_avg(x_sq, ith_x_sq_avg, waittimes, time)
            ith_y_sq_avg = new_vol_dyn.running_abundance_avg(y_sq, ith_y_sq_avg, waittimes, time)
            ith_z_sq_avg = new_vol_dyn.running_abundance_avg(z_sq, ith_z_sq_avg, waittimes, time)
            
            #----------------------------------------------------------
            
            #-----------------------------------------
            #Conc averages
            
            temp_conc_x_average = x * new_vol_dyn.temp_lin_one_over_vol_average(V0, waittimes, interval_time) / waittimes
            ith_conc_x_avg = new_vol_dyn.running_abundance_avg(temp_conc_x_average, ith_conc_x_avg, waittimes, time)
            
            temp_conc_y_average = y * new_vol_dyn.temp_lin_one_over_vol_average(V0, waittimes, interval_time) / waittimes
            ith_conc_y_avg = new_vol_dyn.running_abundance_avg(temp_conc_y_average, ith_conc_y_avg, waittimes, time)
            
            temp_conc_z_average = z * new_vol_dyn.temp_lin_one_over_vol_average(V0, waittimes, interval_time)/ waittimes
            ith_conc_z_avg = new_vol_dyn.running_abundance_avg(temp_conc_z_average, ith_conc_z_avg, waittimes, time)
            
            temp_xz_average = x * z * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
            ith_xz_v2_avg = new_vol_dyn.running_abundance_avg(temp_xz_average, ith_xz_v2_avg, waittimes, time)
            
            temp_yz_average = y * z * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
            ith_yz_v2_avg = new_vol_dyn.running_abundance_avg(temp_yz_average, ith_yz_v2_avg, waittimes, time)
            
            temp_x_sq_average = x *x * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
            ith_x_sq_v2_avg = new_vol_dyn.running_abundance_avg(temp_x_sq_average, ith_x_sq_v2_avg, waittimes, time)
            
            temp_y_sq_average = y *y * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
            ith_y_sq_v2_avg = new_vol_dyn.running_abundance_avg(temp_y_sq_average, ith_y_sq_v2_avg, waittimes, time)
            
            temp_z_sq_average = z *z * new_vol_dyn.temp_lin_one_over_vol_sq_average(V0, waittimes, interval_time)/ waittimes
            ith_z_sq_v2_avg = new_vol_dyn.running_abundance_avg(temp_z_sq_average, ith_z_sq_v2_avg, waittimes, time)
            
            
            
            
            
            
            #----------------------------------------
            
            
            
            
            x_birth_rate = 2*lamda * z / (k + x)
            x_death_rate = z * x
            
            y_birth_rate = lamda * z / (k + x)
            y_death_rate = z * y
            
            z_birth_rate = lamda_z
            z_death_rate = beta_z * z
            
            w_birth_rate = 0 #System 5 has no w
            w_death_rate = 0



            u_event = random.uniform(0,1)
            
            #r_t vol indep so its the same as the one computed above before volume was updated
            
            x_birth_prob = x_birth_rate / r_t
            x_death_prob = (x_birth_rate + x_death_rate) / r_t
            
            y_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate) /r_t
            y_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate) /r_t
            
            z_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate + z_birth_rate) /r_t
            z_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                            + z_birth_rate + z_death_rate) /r_t
                
            w_birth_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                            + z_birth_rate + z_death_rate + w_birth_rate) /r_t
            
            w_death_prob = (x_birth_rate + x_death_rate + y_birth_rate + y_death_rate\
                            + z_birth_rate + z_death_rate + w_birth_rate + w_death_rate) /r_t
                
            if u_event < x_birth_prob:
                x += 1
             
    
            elif u_event < x_death_prob:
                x += -1
                
               
            elif u_event < y_birth_prob:
                y += 1
                
            elif u_event < y_death_prob:
                y += -1
                
                
            elif u_event < z_birth_prob:
                
                z += 1
                
                
            elif u_event < z_death_prob:
              
                z += -1
            
            elif u_event < w_birth_prob:
                
                w += 1
                
            elif u_event < w_death_prob:
                
                w += -1
            
                
                
            xz = x * z
            yz = y * z 
            
            x_sq = x ** 2
            y_sq = y ** 2
            z_sq = z ** 2
    
    if ith_conc_x_avg > 0.001 and ith_conc_y_avg > 0.001 and ith_conc_z_avg > 0.001:
        
        eta_xz_conc = (ith_xz_v2_avg / (ith_conc_x_avg * ith_conc_z_avg)) - 1
        eta_yz_conc = (ith_yz_v2_avg / (ith_conc_y_avg * ith_conc_z_avg)) - 1
        
        eta_xx_conc = (ith_x_sq_v2_avg / (ith_conc_x_avg * ith_conc_x_avg)) - 1
        eta_yy_conc = (ith_y_sq_v2_avg / (ith_conc_y_avg * ith_conc_y_avg)) - 1
        eta_zz_conc = (ith_z_sq_v2_avg / (ith_conc_z_avg * ith_conc_z_avg)) - 1

        

        
        eta_xz_numbers = (ith_xz_avg / (ith_x_avg * ith_z_avg)) - 1
        eta_yz_numbers = (ith_yz_avg / (ith_y_avg * ith_z_avg)) - 1
        
        eta_xx_numbers = (ith_x_sq_avg / (ith_x_avg * ith_x_avg)) - 1
        eta_yy_numbers = (ith_y_sq_avg / (ith_y_avg * ith_y_avg)) - 1
        eta_zz_numbers = (ith_z_sq_avg / (ith_z_avg * ith_z_avg)) - 1

        #print(eta_zz_conc)

        if eta_xx_conc*eta_zz_conc > 0.0000001 and eta_xx_conc*eta_zz_conc < 1000000000:
            pearson_xz_conc = eta_xz_conc / np.sqrt(eta_xx_conc*eta_zz_conc)
            pearson_yz_conc = eta_yz_conc / np.sqrt(eta_yy_conc*eta_zz_conc)

            pearson_xz_numbers = eta_xz_numbers / np.sqrt(eta_xx_numbers*eta_zz_numbers)
            pearson_yz_numbers = eta_yz_numbers / np.sqrt(eta_yy_numbers*eta_zz_numbers)
        
        else:
            #print(ith_z_sq_v2_avg)
            #print(eta_zz_conc)
            #print(ith_conc_z_avg)
            print("YO")

            eta_xz_conc = -501
            eta_yz_conc = -501
            
            pearson_xz_conc = -501
            pearson_yz_conc = -501
            
            eta_xz_numbers = -501
            eta_yz_numbers = -501
            
            pearson_xz_numbers = -501
            pearson_yz_numbers = -501



    else:
        print(ith_conc_x_avg)
        print(ith_conc_y_avg)
        print(ith_conc_z_avg)
        print(ith_z_avg)

        
        eta_xz_conc = -501
        eta_yz_conc = -501
        
        pearson_xz_conc = -501
        pearson_yz_conc = -501
        
        eta_xz_numbers = -501
        eta_yz_numbers = -501
        
        pearson_xz_numbers = -501
        pearson_yz_numbers = -501
        
    return eta_xz_conc, eta_yz_conc, pearson_xz_conc, pearson_yz_conc ,eta_xz_numbers, eta_yz_numbers, pearson_xz_numbers, pearson_yz_numbers, lamda, lamda_z, lamda_w, beta_x, beta_y, beta_z, beta_w, k

            
def parallel_s5_v1(inputs):
    lamda2 = inputs[0]
    lamda_z2 = inputs[1]
    lamda_w2 = inputs[2]
    beta_x2 = inputs[3]
    beta_y2 = beta_x2
    beta_z2 = inputs[4]
    beta_w2 = inputs[5]
    k2 = inputs[6]

    a = np.log(2) #Allows for cell to at most double per interval of 1 second; so that it can be halved after 1 second
    
    V02 = 1
    Vmax2 = 2 * V02 #Other than vol_dynamic 4, volume dynamics chosen to allow volume to at most double


    products2 = [lamda2, lamda_z2, lamda_w2  ,  beta_x2 ,beta_y2, \
            beta_z2,beta_w2,  k2, V02,Vmax2,  a, 0,0, 1,  1, 1, 1, jump_time_1_factor]
    
    
    
    
    #jump_times, stay_prob, Vmax = gaussian_division(jump_time_1_factor) #Uncomment for vol_dyn_4

    eta_xz_net_conc = []
    eta_yz_net_conc = []
    pearson_xz_net_conc = []
    pearson_yz_net_conc  = []
    
    
    eta_xz_error_net_conc = []
    eta_yz_error_net_conc = []
    pearson_xz_error_net_conc = []
    pearson_yz_error_net_conc = []
    
    eta_xz_net_numbers = []
    eta_yz_net_numbers = []
    pearson_xz_net_numbers = []
    pearson_yz_net_numbers  = []
    
    
    eta_xz_error_net_numbers = []
    eta_yz_error_net_numbers = []
    pearson_xz_error_net_numbers = []
    pearson_yz_error_net_numbers = []
    
    
    n = number_of_cores
    temp_eta_xz_conc = []
    temp_eta_yz_conc = []
    
    temp_pearson_xz_conc = []
    temp_pearson_yz_conc = []
    
    temp_eta_xz_numbers = []
    temp_eta_yz_numbers = []
    
    temp_pearson_xz_numbers = []
    temp_pearson_yz_numbers = []
    
    
    AA = 1
    number_of_simulations = 0
    
    
    
    #products2 = [lamda, lamda_z, lamda_w  ,  beta_x ,beta_y, \
    #        beta_z,beta_w,  k, V0,Vmax,  a, 0,0, 1,  1, 1, 1, jump_time_1_factor]
    
    inputs3 = []
    for i in range(number_of_cores):
        inputs3.append(products2)

    while (AA > 0):
        number_of_simulations += n
        
        
        #pool here
        #pool = multiprocessing.Pool(processes = number_of_cores) #first argument after .py file is number of cores
        result = pool.map(s5_v1_covariance, inputs3)
        
        
        #pool.close()
        for _ in range(len(result)):
    
            #print(_)
            eta_xz_conc, eta_yz_conc, pearson_xz_conc, pearson_yz_conc, eta_xz_numbers, eta_yz_numbers, pearson_xz_numbers, pearson_yz_numbers, lamda, lamda_z, lamda_w, beta_x, beta_y, beta_z, beta_w, k = result[_]  #s5_v1_covariance(lamda, lamda_z, lamda_w  ,  beta_x ,beta_y, \
                    #beta_z,beta_w,  k, V0,Vmax,  a, jump_times, stay_prob, 1,  1, 1, 1, jump_time_1_factor)
                
            
            temp_eta_xz_conc.append(eta_xz_conc)
            temp_eta_yz_conc.append(eta_yz_conc)
            temp_pearson_xz_conc.append(pearson_xz_conc)
            temp_pearson_yz_conc.append(pearson_yz_conc)
            
            temp_eta_xz_numbers.append(eta_xz_numbers)
            temp_eta_yz_numbers.append(eta_yz_numbers)
            temp_pearson_xz_numbers.append(pearson_xz_numbers)
            temp_pearson_yz_numbers.append(pearson_yz_numbers)
            
            if eta_xz_conc == -501:
                temp_eta_xz_conc = [-501, -501, -501]

        etaxz_conc_mean = np.mean(temp_eta_xz_conc)
        etayz_conc_mean = np.mean(temp_eta_yz_conc)
        etaxz_conc_err = np.std(temp_eta_xz_conc) * 2 / (len(temp_eta_xz_conc)-1)**0.5
        etayz_conc_err = np.std(temp_eta_yz_conc) * 2 / (len(temp_eta_yz_conc)-1)**0.5
        
        etaxz_num_mean = np.mean(temp_eta_xz_numbers)
        etayz_num_mean = np.mean(temp_eta_yz_numbers)
        etaxz_num_err = np.std(temp_eta_xz_numbers) * 2 / (len(temp_eta_xz_numbers)-1)**0.5
        etayz_num_err = np.std(temp_eta_yz_numbers) * 2 / (len(temp_eta_yz_numbers)-1)**0.5


        
        if number_of_simulations > number_of_simulations_final - 1:
            #pool.close()
            AA = 0

    eta_xz_net_conc.append(np.mean(temp_eta_xz_conc))
    eta_yz_net_conc.append(np.mean(temp_eta_yz_conc))
    eta_xz_error_net_conc.append(np.std(temp_eta_xz_conc) * 2 / (len(temp_eta_xz_conc)-1)**0.5 )
    eta_yz_error_net_conc.append(np.std(temp_eta_yz_conc) * 2 / (len(temp_eta_yz_conc)-1)**0.5 )
    
    eta_xz_net_numbers.append(np.mean(temp_eta_xz_numbers))
    eta_yz_net_numbers.append(np.mean(temp_eta_yz_numbers))
    eta_xz_error_net_numbers.append(np.std(temp_eta_xz_numbers) * 2 / (len(temp_eta_xz_numbers)-1)**0.5)
    eta_yz_error_net_numbers.append(np.std(temp_eta_yz_numbers) * 2 / (len(temp_eta_yz_numbers)-1)**0.5)
    
    
    pearson_xz_net_conc.append(np.mean(temp_pearson_xz_conc))
    pearson_yz_net_conc.append(np.mean(temp_pearson_yz_conc))
    pearson_xz_error_net_conc.append(np.std(temp_pearson_xz_conc) * 2 / (len(temp_pearson_xz_conc)-1)**0.5)
    pearson_yz_error_net_conc.append(np.std(temp_pearson_yz_conc) * 2 / (len(temp_pearson_yz_conc)-1)**0.5)
    
    pearson_xz_net_numbers.append(np.mean(temp_pearson_xz_numbers))
    pearson_yz_net_numbers.append(np.mean(temp_pearson_yz_numbers))
    pearson_xz_error_net_numbers.append(np.std(temp_pearson_xz_numbers) * 2 / (len(temp_pearson_xz_numbers)-1)**0.5)
    pearson_yz_error_net_numbers.append(np.std(temp_pearson_yz_numbers) * 2 / (len(temp_pearson_yz_numbers)-1)**0.5)

    
    
    return  eta_xz_net_conc, eta_yz_net_conc, eta_xz_error_net_conc, eta_yz_error_net_conc, pearson_xz_net_conc, pearson_yz_net_conc, pearson_xz_error_net_conc, pearson_yz_error_net_conc, \
        eta_xz_net_numbers, eta_yz_net_numbers, eta_xz_error_net_numbers, eta_yz_error_net_numbers, pearson_xz_net_numbers, pearson_yz_net_numbers, pearson_xz_error_net_numbers, pearson_yz_error_net_numbers,\
            lamda, lamda_z, lamda_w, beta_x, beta_y, beta_z, beta_w, k, number_of_simulations

#----------------------------------------------

lamdaa = np.loadtxt(path_2 + '/system_' +system_number +'/vol_dynamic_'+volume_number+'/results/bad_parameters/s'+system_number+'_v'+volume_number+'_bad_conc_lamda.csv')
lamda_wa = np.loadtxt(path_2 + '/system_' +system_number +'/vol_dynamic_'+volume_number+'/results/bad_parameters/s'+system_number+'_v'+volume_number+'_bad_conc_lamda_w.csv')
lamda_za = np.loadtxt(path_2 + '/system_' +system_number +'/vol_dynamic_'+volume_number+'/results/bad_parameters/s'+system_number+'_v'+volume_number+'_bad_conc_lamda_z.csv')

beta_xa = np.loadtxt(path_2 + '/system_' +system_number +'/vol_dynamic_'+volume_number+'/results/bad_parameters/s'+system_number+'_v'+volume_number+'_bad_conc_beta_x.csv')
beta_ya = np.loadtxt(path_2 + '/system_' +system_number +'/vol_dynamic_'+volume_number+'/results/bad_parameters/s'+system_number+'_v'+volume_number+'_bad_conc_beta_y.csv')
beta_za = np.loadtxt(path_2 + '/system_' +system_number +'/vol_dynamic_'+volume_number+'/results/bad_parameters/s'+system_number+'_v'+volume_number+'_bad_conc_beta_z.csv')
beta_wa = np.loadtxt(path_2 + '/system_' +system_number +'/vol_dynamic_'+volume_number+'/results/bad_parameters/s'+system_number+'_v'+volume_number+'_bad_conc_beta_w.csv')
ka = np.loadtxt(path_2 + '/system_' +system_number +'/vol_dynamic_'+volume_number+'/results/bad_parameters/s'+system_number+'_v'+volume_number+'_bad_conc_k.csv')

number_of_simulations_previous = np.loadtxt(path_2 + '/system_' +system_number +'/vol_dynamic_'+volume_number+'/results/bad_parameters/s'+system_number+'_v'+volume_number+'_bad_conc_number_of_simulations.csv')


if lamdaa.ndim > 0:
    blank = np.transpose (np.zeros((len(lamdaa), 7) ) )
    blank[ 0 , : ] = lamdaa
    blank[1 ,  :] = lamda_za
    blank[2 , :  ] = lamda_wa
    blank[ 3 , : ] = beta_xa
    #blank[4 , : ] = beta_ya
    blank[ 4 , :] = beta_za
    blank[5, :] = beta_wa
    blank[6, :] = ka

    blank = np.transpose(blank)

    products = list(blank)
    # =============================================================================


    number_of_parameters = len(lamdaa)


    pool = multiprocessing.Pool(processes = number_of_cores) #first argument after .py file is number of cores

    result = []
    for i in range(number_of_parameters):
        print(system_number + volume_number)
        print(i+1)
        number_of_simulations_final = 2*number_of_simulations_previous[i]
        single_result = parallel_s5_v1(products[i])
        result.append(single_result)
    pool.close()
    
else:
    blank = [lamdaa, lamda_za, lamda_wa, beta_xa, beta_za, beta_wa, ka]

    #blank = np.transpose(blank)

    products = blank
    
        # =============================================================================


    number_of_parameters = 1


    pool = multiprocessing.Pool(processes = number_of_cores) #first argument after .py file is number of cores

    result = []
    for i in range(number_of_parameters):
        print(system_number + volume_number)
        print(i+1)
        number_of_simulations_final = 2*number_of_simulations_previous
        single_result = parallel_s5_v1(products)
        result.append(single_result)
    pool.close()
    
eta_xz, eta_yz, eta_xz_error, eta_yz_error, pearson_xz, pearson_yz, pearson_xz_error, pearson_yz_error,\
    eta_xz_numbers, eta_yz_numbers, eta_xz_error_numbers, eta_yz_error_numbers, pearson_xz_numbers, pearson_yz_numbers, pearson_xz_error_numbers, pearson_yz_error_numbers, lamda, lamda_z, lamda_w, beta_x, beta_y, beta_z, beta_w, k, number_of_simulations = new_vol_dyn.flatten_3d(result)



#Original save path
#save_path = path_2 + '/system_' +system_number+'/vol_dynamic_'+volume_number+ '/results/split_'+split_number+' _s'+system_number+'_v'+volume_number

#Rereun save path
save_path =  path_2 + '/system_' +system_number+'/vol_dynamic_'+volume_number+ '/results/bad_parameters/rerun/rerun_s'+ system_number+'_v'+volume_number


np.savetxt(save_path + '_eta_xz.csv', eta_xz, delimiter = ',')
np.savetxt(save_path + '_eta_yz.csv', eta_yz, delimiter = ',')
np.savetxt(save_path + '_eta_xz_error.csv', eta_xz_error, delimiter = ',')
np.savetxt(save_path + '_eta_yz_error.csv', eta_yz_error, delimiter = ',')

np.savetxt(save_path + '_pearson_xz.csv', pearson_xz, delimiter = ',')
np.savetxt(save_path + '_pearson_yz.csv', pearson_yz, delimiter = ',')
np.savetxt(save_path + '_pearson_xz_error.csv', pearson_xz_error, delimiter = ',')
np.savetxt(save_path + '_pearson_yz_error.csv', pearson_yz_error, delimiter = ',')

np.savetxt(save_path + '_lamda.csv', lamda, delimiter = ',')
np.savetxt(save_path + '_lamda_z.csv', lamda_z, delimiter = ',')
np.savetxt(save_path + '_lamda_w.csv', lamda_w, delimiter = ',')

np.savetxt(save_path + '_beta_x.csv', beta_x, delimiter = ',')
np.savetxt(save_path + '_beta_y.csv', beta_y, delimiter = ',')
np.savetxt(save_path + '_beta_z.csv', beta_z, delimiter = ',')
np.savetxt(save_path + '_beta_w.csv', beta_w, delimiter = ',')

np.savetxt(save_path + '_k.csv', k, delimiter = ',')


np.savetxt(save_path + '_eta_xz_numbers.csv', eta_xz_numbers, delimiter = ',')
np.savetxt(save_path + '_eta_yz_numbers.csv', eta_yz_numbers, delimiter = ',')
np.savetxt(save_path + '_eta_xz_error_numbers.csv', eta_xz_error_numbers, delimiter = ',')
np.savetxt(save_path + '_eta_yz_error_numbers.csv', eta_yz_error_numbers, delimiter = ',')

np.savetxt(save_path + '_pearson_xz_numbers.csv', pearson_xz_numbers, delimiter = ',')
np.savetxt(save_path + '_pearson_yz_numbers.csv', pearson_yz_numbers, delimiter = ',')
np.savetxt(save_path + '_pearson_xz_error_numbers.csv', pearson_xz_error_numbers, delimiter = ',')
np.savetxt(save_path + '_pearson_yz_error_numbers.csv', pearson_yz_error_numbers, delimiter = ',')


np.savetxt(save_path + '_number_of_simulations.csv', number_of_simulations, delimiter = ',')






finish= timer.perf_counter()

print(f'Finished in {round(finish - start , 2) } second(s) i.e. {round((finish - start)/60 , 2) } minute(s) i.e. \
      {round((finish - start)/3600 , 2) } hour(s)')
         
            
            
        

