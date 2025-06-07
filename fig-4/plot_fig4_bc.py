import matplotlib.pyplot as plt
import numpy as np
import pickle

#INPUT 
number_of_positions = 10
bin_time = 5./60 

pixels_cells = []
cfp_cells = []
yfp_cells = []
rfp_cells = []
frames_cells = []
areas_cells = []
lengths_cells = []
growth_rate_cells = []
growth_rate_smooth_cells = []
time_to_divide = []
rfp_smooth_cells = []
yfp_smooth_cells = []
cfp_smooth_cells = []

for p in range(12, 12 + number_of_positions):
    
    pixels_cells_p = []
    cfp_cells_p = []
    yfp_cells_p = []
    rfp_cells_p = []
    frames_cells_p = []
    areas_cells_p = []
    lengths_cells_p = []
    growth_rate_cells_p = []
    growth_rate_smooth_cells_p = []
    
    with open('../data/delta/EJS2/yfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_yfp_load = pickle.load(f)
        
    with open('../data/delta/EJS2/cfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_cfp_load = pickle.load(f)
    
    with open('../data/delta/EJS2/rfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_rfp_load = pickle.load(f)
        
    with open('../data/delta/EJS2/lengths_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_lengths_load = pickle.load(f)
        
    with open('../data/delta/EJS2/areas_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_areas_load = pickle.load(f)
        
    with open('../data/delta/EJS2/frames_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_frames_load = pickle.load(f)
        
    with open('../data/delta/EJS2/frames_purged_xpixels' +str(p) + '-purge2.pkl', 'rb') as f:
        final_xpixels_load = pickle.load(f)
            

        
    #final_areas_load = final_lengths_load
    for cell in range(0,len(final_cfp_load)):    
        if len(final_lengths_load[cell]) > 0 :
            
            
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
                    cfp_cells_p.append(np.array(final_cfp_load[cell])[:division_times[-1]])
                    yfp_cells_p.append(np.array(final_yfp_load[cell])[:division_times[-1]])
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
                    cfp_cells_p.append(np.array(final_cfp_load[cell])[2:division_times[-1]])
                    yfp_cells_p.append(np.array(final_yfp_load[cell])[2:division_times[-1]])
                    rfp_cells_p.append(np.array(final_rfp_load[cell])[2:division_times[-1]])
                    frames_cells_p.append(np.array(final_frames_load[cell])[2:division_times[-1]])
                    areas_cells_p.append(np.array(final_areas_load[cell])[2:division_times[-1]])
                    lengths_cells_p.append(np.array(final_lengths_load[cell])[2:division_times[-1]])                  
                        
                            
        
                N = 5 #moving average
                temp_growth_rates_smooth = np.convolve(temp_growth_rates, np.ones(N)/N, mode='valid')/bin_time
                growth_rate_smooth_cells_p.append(temp_growth_rates_smooth)
                growth_rate_cells_p.append(np.array(temp_growth_rates)/bin_time)
            
    if len(pixels_cells_p) > 0 : 
        
        pixels_cells_p_array = np.array(pixels_cells_p)
        unique_cells = np.unique(pixels_cells_p_array)
        for k in range(len(unique_cells)):
            cfp_temp = []
            yfp_temp = []
            rfp_temp = []
            pixels_temp = []
            frames_temp =[]
            lengths_temp = []
            areas_temp = []
            growth_rate_temp = []
            growth_rate_smooth_temp = []
            where_cells_is = np.where(pixels_cells_p_array == unique_cells[k])[0]

            for kk in range(len(where_cells_is)):
                cell_index = where_cells_is[kk]
                
                for jjj in range(len(  cfp_cells_p[cell_index]  ) ):
                    cfp_temp.append(cfp_cells_p[cell_index][jjj])
                    yfp_temp.append(yfp_cells_p[cell_index][jjj])
                    rfp_temp.append(rfp_cells_p[cell_index][jjj])
                    frames_temp.append(frames_cells_p[cell_index][jjj])
                    areas_temp.append(areas_cells_p[cell_index][jjj])
                    lengths_temp.append(lengths_cells_p[cell_index][jjj])
                    growth_rate_temp.append(growth_rate_cells_p[cell_index][jjj])
                for jjj in range( len(growth_rate_smooth_cells_p[cell_index]) ):
                    growth_rate_smooth_temp.append(growth_rate_smooth_cells_p[cell_index][jjj])

            
            pixels_cells.append(unique_cells[k])
            cfp_cells.append(np.array(cfp_temp))
            yfp_cells.append(np.array(yfp_temp))
            rfp_cells.append(np.array(rfp_temp))
            frames_cells.append(np.array(frames_temp))
            areas_cells.append(np.array(areas_temp))
            lengths_cells.append(np.array(lengths_temp))
            growth_rate_cells.append(np.array(growth_rate_temp))
            growth_rate_smooth_cells.append(growth_rate_smooth_temp)
            
            M = 1 #moving average
            temp_rfp_smooth = np.convolve( rfp_temp, np.ones(M)/M, mode='valid')
            
            rfp_smooth_cells.append(np.array(temp_rfp_smooth))
            
            temp_cfp_smooth = np.convolve( cfp_temp, np.ones(M)/M, mode='valid')
            
            cfp_smooth_cells.append(np.array(temp_cfp_smooth))
            
            temp_yfp_smooth = np.convolve( yfp_temp, np.ones(M)/M, mode='valid')
            
            yfp_smooth_cells.append(np.array(temp_yfp_smooth))




generation_time = 32.433
CELL = 128  
fig, ax = plt.subplots(1, 1, figsize = (5,2))
t1 = np.array(range(len(yfp_smooth_cells[CELL])))*5./generation_time
t2 = np.array(range(len(growth_rate_smooth_cells[CELL])))*5./generation_time
ax.plot(t1[:] - t1[0], 1*rfp_smooth_cells[CELL][:]/np.average(rfp_smooth_cells[CELL]), color = 'r')

ax.set_xlabel('Time (generations)')
ax.set_ylabel('Fluorescence' + '\n' + '(mean normalized)')
ax1 = ax.twinx()
ax1.plot( t2[:] - t2[0] , growth_rate_smooth_cells[CELL][:])
ax1.set_ylabel('Growth rate (1/h)', rotation=270,labelpad=15)

ax.set_ylim([0.43,1.8])
ax1.set_ylim([0.43,1.8])


plt.tight_layout()

plt.show()

