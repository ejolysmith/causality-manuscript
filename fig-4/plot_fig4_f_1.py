import matplotlib.pyplot as plt
import numpy as np
import pickle



#INPUT 
number_of_positions = 10
bin_time = 5 #5min

pixels_cells = []
yfp_cells = []
frames_cells = []
areas_cells = []
lengths_cells = []
growth_rate_cells = []
growth_rate_smooth_cells = []
time_to_divide = []
yfp_smooth_cells = []

path = '../Data/EJS1/'
for p in range(0, 0 + number_of_positions):
    
    pixels_cells_p = []
    yfp_cells_p = []
    frames_cells_p = []
    areas_cells_p = []
    lengths_cells_p = []
    growth_rate_cells_p = []
    growth_rate_smooth_cells_p = []
    
        
    with open(path + 'yfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_yfp_load = pickle.load(f)
            
    with open(path +'lengths_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_lengths_load = pickle.load(f)
        
    with open(path +'areas_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_areas_load = pickle.load(f)
        
    with open(path +'frames_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_frames_load = pickle.load(f)
        
    with open(path +'frames_purged_xpixels' +str(p) + '-purge2.pkl', 'rb') as f:
        final_xpixels_load = pickle.load(f)
    
            

        
    #final_areas_load = final_lengths_load
    for cell in range(0,len(final_yfp_load)):    
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
                    yfp_cells_p.append(np.array(final_yfp_load[cell])[:division_times[-1]])
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
                    yfp_cells_p.append(np.array(final_yfp_load[cell])[2:division_times[-1]])
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
            yfp_temp = []
            pixels_temp = []
            frames_temp =[]
            lengths_temp = []
            areas_temp = []
            growth_rate_temp = []
            growth_rate_smooth_temp = []
            where_cells_is = np.where(pixels_cells_p_array == unique_cells[k])[0]
            #pixels_temp.append(unique_cells[k])
            for kk in range(len(where_cells_is)):
                cell_index = where_cells_is[kk]
                
                for jjj in range(len(  yfp_cells_p[cell_index]  ) ):
                    yfp_temp.append(yfp_cells_p[cell_index][jjj])
                    frames_temp.append(frames_cells_p[cell_index][jjj])
                    areas_temp.append(areas_cells_p[cell_index][jjj])
                    lengths_temp.append(lengths_cells_p[cell_index][jjj])
                    growth_rate_temp.append(growth_rate_cells_p[cell_index][jjj])
                for jjj in range( len(growth_rate_smooth_cells_p[cell_index]) ):
                    growth_rate_smooth_temp.append(growth_rate_smooth_cells_p[cell_index][jjj])

            
            pixels_cells.append(unique_cells[k])
            yfp_cells.append(np.array(yfp_temp))
            frames_cells.append(np.array(frames_temp))
            areas_cells.append(np.array(areas_temp))
            lengths_cells.append(np.array(lengths_temp))
            growth_rate_cells.append(np.array(growth_rate_temp))
            growth_rate_smooth_cells.append(growth_rate_smooth_temp)



generation_time = 27.57
CELL = 25  #5 11 27 great 32   36!
A = 30
fig, ax = plt.subplots(1, 1, figsize = (4,1.7))
t1 = np.array(range(len(yfp_cells[CELL])))*5./generation_time
t2 = np.array(range(len(yfp_cells[CELL])))*5./generation_time

ax.set_xlabel('Time (generations)')
ax.set_ylabel('Concentration (a.u.)')

ax.plot( t2[A:] - t2[A] ,2*yfp_cells[CELL][A:], color = 'y')


ax.set_xlim([0,19])
ax.set_ylim([0, 300])


plt.tight_layout()

plt.show()





