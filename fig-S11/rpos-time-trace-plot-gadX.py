#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:06:12 2023

@author: euan
"""

#import delta
#import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pickle
from uncertainties import ufloat
from uncertainties.umath import sqrt as usqrt
#gpus = tf.config.experimental.list_physical_devices('GPU')
#for gpu in gpus:
#  tf.config.experimental.set_memory_growth(gpu, True)
import math

from scipy.io import loadmat
import random


#INPUT 
number_of_positions = 15
bin_time = 8 #8min

pixels_cells = []
gfp_cells = []
#yfp_cells = []
rfp_cells = []
frames_cells = []
areas_cells = []
lengths_cells = []
growth_rate_cells = []
growth_rate_smooth_cells = []
rfp_smooth_cells = []
gfp_smooth_cells = []
time_to_divide = []


path = '../data/delta/PA64/'
for p in range(22, 22 + number_of_positions):
    
    pixels_cells_p = []
    gfp_cells_p = []
    #yfp_cells_p = []
    rfp_cells_p = []
    frames_cells_p = []
    areas_cells_p = []
    lengths_cells_p = []
    growth_rate_cells_p = []
    growth_rate_smooth_cells_p = []
    
    #with open('yfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
    #    final_yfp_load = pickle.load(f)
        
    with open(path + 'gfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_gfp_load = pickle.load(f)
    
    with open(path +'rfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_rfp_load = pickle.load(f)
        
    with open(path +'lengths_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_lengths_load = pickle.load(f)
        
    with open(path +'areas_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_areas_load = pickle.load(f)
        
    with open(path +'frames_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_frames_load = pickle.load(f)
        
    with open(path +'frames_purged_xpixels' +str(p) + '-purge2.pkl', 'rb') as f:
        final_xpixels_load = pickle.load(f)
    

    #final_areas_load = final_lengths_load
    for cell in range(0,len(final_gfp_load)):    
        if len(final_lengths_load[cell]) > 0 and len(final_gfp_load[cell]) == len(final_rfp_load[cell]):
            
            
            cell_length = final_lengths_load[cell]
            #Getting growth rates:
            division_times = []
            for i in range(len(final_lengths_load[cell])-1):
                if final_lengths_load[cell][i+1]  < 0.8*final_lengths_load[cell][i]:    #This finds the divisions
                    division_times.append(i+1)
            for ii in range(1,len(division_times)):
                time_to_divide.append( division_times[ii] - division_times[ii-1])
            growth_rates_per_cycle = []
            first_div = 0
            if len(division_times) > 0:
                if division_times[0] > 1 :
                    temp_growth_rates = []
                    growth_rate  =  ( np.log(cell_length[1]/cell_length[0]) )/1
                    temp_growth_rates.append(growth_rate)
                    
                    current_cycle = 0    
                    
                    
                    
                    for i in range(1,division_times[-1]):
                        if current_cycle == 0:
                            if i < division_times[current_cycle] - 1 :
                                growth_rate  = (np.log(cell_length[i+1]/cell_length[i-1]))/2
                                temp_growth_rates.append(growth_rate)
                            else:
                                growth_rate  = ( np.log(cell_length[i]/cell_length[i-1]) )/1
                                temp_growth_rates.append(growth_rate)
                                current_cycle = current_cycle + 1
                        else:
                            if i == division_times[current_cycle - 1] :
                                growth_rate  =  ( np.log(cell_length[i+1]/cell_length[i]) )/1
                                temp_growth_rates.append(growth_rate)
                            elif i < division_times[current_cycle] - 1 :
                                growth_rate  = ( np.log(cell_length[i+1]/cell_length[i-1]) )/2
                                temp_growth_rates.append(growth_rate)
                            else:
                                growth_rate  = ( np.log(cell_length[i]/cell_length[i-1]) )/1
                                temp_growth_rates.append(growth_rate)
                                current_cycle = current_cycle + 1
                    
                    
                    pixels_cells_p.append(final_xpixels_load[cell])
                    gfp_cells_p.append(np.array(final_gfp_load[cell])[:division_times[-1]])
                    #yfp_cells_p.append(np.array(final_yfp_load[cell])[:division_times[-1]])
                    rfp_cells_p.append(np.array(final_rfp_load[cell])[:division_times[-1]])
                    frames_cells_p.append(np.array(final_frames_load[cell])[:division_times[-1]])
                    areas_cells_p.append(np.array(final_areas_load[cell])[:division_times[-1]])
                    lengths_cells_p.append(np.array(final_lengths_load[cell])[:division_times[-1]])
                    
                    
                else:
                    temp_growth_rates = []
                
                    
                    growth_rate = ( np.log(cell_length[2]/cell_length[1]) )/1
                    temp_growth_rates.append(growth_rate)
                    
                    current_cycle = 0    
                    
                    for i in range(2,division_times[-1]):
                        if current_cycle == 0:
                            if i < division_times[current_cycle] - 1 :
                                growth_rate  = ( np.log(cell_length[i+1]/cell_length[i-1]) )/2
                                temp_growth_rates.append(growth_rate)
                            else:
                                growth_rate  = ( np.log(cell_length[i]/cell_length[i-1]) )/1
                                temp_growth_rates.append(growth_rate)
                                current_cycle = current_cycle + 1
                        else:
                            if i == division_times[current_cycle - 1] :
                                growth_rate  =  ( np.log(cell_length[i+1]/cell_length[i]) )/1
                                temp_growth_rates.append(growth_rate)
                            elif i < division_times[current_cycle] - 1 :
                                growth_rate  = ( np.log(cell_length[i+1]/cell_length[i-1]) )/2
                                temp_growth_rates.append(growth_rate)
                            else:
                                growth_rate  = ( np.log(cell_length[i]/cell_length[i-1]) )/1
                                temp_growth_rates.append(growth_rate)
                                current_cycle = current_cycle + 1
                                
                    
                    pixels_cells_p.append(final_xpixels_load[cell])
                    gfp_cells_p.append(np.array(final_gfp_load[cell])[2:division_times[-1]])
                    #yfp_cells_p.append(np.array(final_yfp_load[cell])[2:division_times[-1]])
                    rfp_cells_p.append(np.array(final_rfp_load[cell])[2:division_times[-1]])
                    frames_cells_p.append(np.array(final_frames_load[cell])[2:division_times[-1]])
                    areas_cells_p.append(np.array(final_areas_load[cell])[2:division_times[-1]])
                    lengths_cells_p.append(np.array(final_lengths_load[cell])[2:division_times[-1]])                  
                    
                        
                            
                #if len(cell_area) - (division_times[-1]+1) > 0:
                #    growth_rate = np.log( final_areas_load[cell][-1]/final_areas_load[cell][division_times[-1]])/(len(final_lengths_load[cell]) - 1 - division_times[-1])
                #    growth_rates_per_cycle.append(growth_rate)
                    
                
                
                #for i in range(division_times[0],len(final_frames_load[cell])):
                #    if first_div == 1 : 
                ##        for j in range(0,len(division_times)):
                 #           if i < division_times[j] and i >= division_times[j-1]:
                #                temp_growth_rates.append(growth_rates_per_cycle[j])
                #    else:
                #        for j in range(0,len(division_times)-1):
                #            if i < division_times[j+1] and i >= division_times[j]:
                ##                temp_growth_rates.append(growth_rates_per_cycle[j])
                                
                #for i in range(division_times[-1], len(final_frames_load[cell])):
                #    temp_growth_rates.append(growth_rates_per_cycle[-1])
        
                inf_or_nan = 0
                #for i in range(len(growth_rates_per_cycle)):
                #    if (math.isnan(growth_rates_per_cycle[i]) is True or math.isinf(growth_rates_per_cycle[i]) is True ):
                #        inf_or_nan = 1
                #       break
                N = 5 #moving average
                temp_growth_rates_smooth = np.convolve(temp_growth_rates, np.ones(N)/N, mode='valid')/bin_time
                if inf_or_nan == 0:
                    
                    growth_rate_smooth_cells_p.append(temp_growth_rates_smooth)
                    growth_rate_cells_p.append(np.array(temp_growth_rates)/bin_time)
                    
           
            
    if len(pixels_cells_p) > 0 : 
        
        growth_rate_smooth_temp = []
        
        pixels_cells_p_array = np.array(pixels_cells_p)
        unique_cells = np.unique(pixels_cells_p_array)
        for k in range(len(unique_cells)):
            gfp_temp = []
            #yfp_temp = []
            rfp_temp = []
            pixels_temp = []
            frames_temp =[]
            lengths_temp = []
            areas_temp = []
            growth_rate_temp = []
            where_cells_is = np.where(pixels_cells_p_array == unique_cells[k])[0]
            #pixels_temp.append(unique_cells[k])
            for kk in range(len(where_cells_is)):
                cell_index = where_cells_is[kk]
                
                for kkk in range(len(  growth_rate_smooth_cells_p[cell_index]  ) ):
                    gfp_temp.append(gfp_cells_p[cell_index][kkk])
                    #yfp_temp.append(yfp_cells_p[cell_index][kkk])
                    rfp_temp.append(rfp_cells_p[cell_index][kkk])
                    frames_temp.append(frames_cells_p[cell_index][kkk])
                    areas_temp.append(areas_cells_p[cell_index][kkk])
                    lengths_temp.append(lengths_cells_p[cell_index][kkk])
                    growth_rate_temp.append(growth_rate_cells_p[cell_index][kkk])
                    growth_rate_smooth_temp.append(growth_rate_smooth_cells_p[cell_index][kkk])

            pixels_cells.append(unique_cells[k])
            gfp_cells.append(np.array(gfp_temp))
            #yfp_cells.append(np.array(yfp_temp))
            rfp_cells.append(np.array(rfp_temp))
            frames_cells.append(np.array(frames_temp))
            areas_cells.append(np.array(areas_temp))
            lengths_cells.append(np.array(lengths_temp))
            growth_rate_cells.append(np.array(growth_rate_temp))
            #growth_rate_smooth_cells.append(growth_rate_smooth_temp)

                
            
            M = 5 #moving average
            temp_rfp_smooth = np.convolve( rfp_temp, np.ones(M)/M, mode='valid')
            
            rfp_smooth_cells.append(np.array(temp_rfp_smooth))
            
            temp_gfp_smooth = np.convolve( gfp_temp, np.ones(M)/M, mode='valid')
            
            gfp_smooth_cells.append(np.array(temp_gfp_smooth))
            
            M = 5
            temp_growth_rates_smooth = np.convolve( growth_rate_temp, np.ones(M)/M, mode='valid')
            
            growth_rate_smooth_cells.append(np.array(temp_growth_rates_smooth)*60)
"""
25
28
29
30
32
34
36
43
48
49
55
58
59
69
"""
generation_time = 32.433

CELL = 198 #36 #36 #198  #13
fig, ax = plt.subplots(1, 1, figsize = (6,2))
a = 0
b = 100
t1 = np.array(range(len(gfp_smooth_cells[CELL][a:b])))*5./generation_time
t2 = np.array(range(len(growth_rate_smooth_cells[CELL][a:b])))*5./generation_time
ax.plot(t2 , growth_rate_smooth_cells[CELL][a:b], color = 'darkred')
ax.set_xlabel('Time (generations)')
ax.set_ylabel('Concentration (a.u.)')

ax1 = ax.twinx()
ax1.plot( t2  ,gfp_smooth_cells[CELL][a:b]/np.average(gfp_smooth_cells[CELL][a:b]), '--', color = '0.5')
ax1.set_ylabel('RpoS activity (a.u.)', rotation=270,labelpad=15)


plt.tight_layout()
#plt.savefig('rpos-for-SI-v8.pdf')

plt.show()
#plt.plot( np.array(range(len(growth_rate_smooth_cells[CELL])))*0.083,  growth_rate_smooth_cells[CELL])

