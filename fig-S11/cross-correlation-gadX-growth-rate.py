import matplotlib.pyplot as plt
import numpy as np
import pickle
from scipy import signal

#INPUT 
number_of_positions = 15
bin_time = 8 #8min

pixels_cells = []
gfp_cells = []
frames_cells = []
areas_cells = []
lengths_cells = []
growth_rate_cells = []
growth_rate_smooth_cells = []
time_to_divide = []
gfp_smooth_cells = []
cross = []
cross_lags = []

path = '../data/delta/PA64/'
for p in range(22, 22 + number_of_positions):
    
    pixels_cells_p = []
    gfp_cells_p = []
    frames_cells_p = []
    areas_cells_p = []
    lengths_cells_p = []
    growth_rate_cells_p = []
    growth_rate_smooth_cells_p = []
    
    with open(path + 'gfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_gfp_load = pickle.load(f)
        
    
    with open(path + 'lengths_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_lengths_load = pickle.load(f)
        
    with open(path + 'areas_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_areas_load = pickle.load(f)
        
    with open(path + 'frames_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_frames_load = pickle.load(f)
        
    with open(path + 'frames_purged_xpixels' +str(p) + '-purge2.pkl', 'rb') as f:
        final_xpixels_load = pickle.load(f)
            

    #final_areas_load = final_lengths_load
    for cell in range(0,len(final_gfp_load)):    
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
                    gfp_cells_p.append(np.array(final_gfp_load[cell])[:division_times[-1]])
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
                    frames_cells_p.append(np.array(final_frames_load[cell])[2:division_times[-1]])
                    areas_cells_p.append(np.array(final_areas_load[cell])[2:division_times[-1]])
                    lengths_cells_p.append(np.array(final_lengths_load[cell])[2:division_times[-1]])                  
                    
        
                growth_rate_cells_p.append(np.array(temp_growth_rates)/bin_time)
                    
           
            
    if len(pixels_cells_p) > 0 : 
        
        
        pixels_cells_p_array = np.array(pixels_cells_p)
        unique_cells = np.unique(pixels_cells_p_array)
        for k in range(len(unique_cells)):
            gfp_temp = []
            pixels_temp = []
            frames_temp =[]
            lengths_temp = []
            areas_temp = []
            growth_rate_temp = []
            where_cells_is = np.where(pixels_cells_p_array == unique_cells[k])[0]

            for kk in range(len(where_cells_is)):
                cell_index = where_cells_is[kk]
                
                for kkk in range(len(  gfp_cells_p[cell_index]  ) ):
                    gfp_temp.append(gfp_cells_p[cell_index][kkk])
                    frames_temp.append(frames_cells_p[cell_index][kkk])
                    areas_temp.append(areas_cells_p[cell_index][kkk])
                    lengths_temp.append(lengths_cells_p[cell_index][kkk])
                    growth_rate_temp.append(growth_rate_cells_p[cell_index][kkk])

        
            pixels_cells.append(unique_cells[k])
            frames_cells.append(np.array(frames_temp))
            areas_cells.append(np.array(areas_temp))
            lengths_cells.append(np.array(lengths_temp))
    
            M = 5 #moving average
            
            
            
            temp_gfp_smooth = np.convolve( gfp_temp, np.ones(M)/M, mode='valid')
            
            gfp_cells.append(np.array(temp_gfp_smooth))

            temp_growth_rates_smooth = np.convolve( growth_rate_temp, np.ones(M)/M, mode='valid')
            
            growth_rate_cells.append(np.array(growth_rate_temp))



    
number_of_cells = len(gfp_cells)



for i in range(number_of_cells):
    for j in range(len(gfp_cells[i])):
        gfp_cells[i][j] = gfp_cells[i][j] #- min_gfp_b


number_of_samples = 1





max_frame = 400
min_frame = 50


#Taking bootstrapping samples of cell distribution
for sample in range(number_of_samples):
    gfp_sample = []
    pixels_sample = []
    frames_sample = []
    lengths_sample = []
    growth_rate_sample = []
    
    for cell in range(number_of_cells):
        random_cell = cell
        for k in range(len(gfp_cells[random_cell])):
            if frames_cells[random_cell][k] > min_frame and frames_cells[random_cell][k] < max_frame:
                gfp_sample.append(gfp_cells[random_cell][k])
                pixels_sample.append(pixels_cells[random_cell])
                frames_sample.append(frames_cells[random_cell][k])
                lengths_sample.append(lengths_cells[random_cell][k])
                growth_rate_sample.append(growth_rate_cells[random_cell][k])
         
    #Turning sample data sets into arrays
    pixels_sample = np.array(pixels_sample)
    gfp_sample = np.array(gfp_sample)
    growth_rate_sample = np.array(growth_rate_sample)
    lengths_sample = np.array(lengths_sample)
    frames_sample = np.array(frames_sample)    
    
    
    
    
        
    #Turning sample data sets into arrays for lost plasmid
    
    #### DRIFT CORRECTION ###
    number_of_frames = max_frame   #Set this to the length of the time trafes

    gfp_time_bins = np.zeros(number_of_frames)
    gfp_time_bins_num = np.zeros(number_of_frames)
    for i in range(len(frames_sample)):
        if frames_sample[i] < number_of_frames :
            gfp_time_bins[int(frames_sample[i])] = gfp_time_bins[int(frames_sample[i])] + gfp_sample[i]
            gfp_time_bins_num[int(frames_sample[i])] = gfp_time_bins_num[int(frames_sample[i])] + 1
    gfp_time_bins = gfp_time_bins/gfp_time_bins_num



    
    #In the following, 50 is set at the initial time trace cut off due to photobleaching.
    #Correcting the time-drift:
        
    Z = np.polyfit(np.array(range(min_frame + 1, len(gfp_time_bins))), gfp_time_bins[min_frame + 1:], 2)
    P = np.poly1d(Z)

    for i in range(len(gfp_sample)):
        if frames_sample[i] < number_of_frames :
            gfp_sample[i] = gfp_sample[i]/P(int(frames_sample[i]))*P(0)
            
    
    #######  Non-even illumination correction    #######
    bsize = 50 #Do we need bins? 
    number_of_bins = int(2050/bsize)

    pixel_bins = []
    gfp_bins = []
    
    for i in range(number_of_bins):
        gfp_average = 0
        
        number = 0
        for j in range(len(pixels_sample)):
            if i*bsize <= pixels_sample[j] < (i+1)*bsize:
                if frames_sample[j] > min_frame and frames_sample[j] < max_frame:
                    gfp_average = gfp_average + gfp_sample[j]#/P_gfp((i+0.5)*bsize)*z_gfp_max
                    
                    number = number + 1
        if number > 0 :
            #print(number)
            
            gfp_average = gfp_average/number
            gfp_bins.append(gfp_average)
            
            pixel_bins.append((i+0.5)*bsize)
            
    z_gfp = np.polyfit(pixel_bins, gfp_bins, 3)





    pix = np.linspace(0,2000, 2000)
    
    P_gfp = np.poly1d(z_gfp)
    z_gfp_max = np.max(P_gfp(pix))
    
    for cell in range(len(gfp_cells)):
        for i in range(len(gfp_cells[cell])):
            gfp_cells[cell][i] = gfp_cells[cell][i]/P_gfp(pixels_sample[i])*z_gfp_max
    
            
                
            
 
cross = []
cross_lags = []

for cell in range(len(gfp_cells)):
    gfp_temp = gfp_cells[cell]
    growth_rate_temp = growth_rate_cells[cell]

    
    M = 5 #moving average
    
    
    
    growth_rate_temp = np.convolve( growth_rate_temp, np.ones(M)/M, mode='same')

    corr = signal.correlate( (gfp_temp - np.average(gfp_temp)), (growth_rate_temp - np.average(growth_rate_temp)), mode = 'full') #- np.average(rfp_temp)*np.average(growth_rate_temp)
    cross_corr1 = np.sum((gfp_temp - np.average(gfp_temp))**2)
    cross_corr2 =  np.sum((growth_rate_temp - np.average(growth_rate_temp))**2)

    lags = signal.correlation_lags(len(gfp_temp), len(gfp_temp))
    ww = np.where(lags == 0)[0]

    corr /= np.sqrt(cross_corr1*cross_corr2)
    cross.append( corr )
    cross_lags.append(lags)

final_cross_lags = np.array(range(-1000,1000))*8./60
final_cross = np.zeros(len(final_cross_lags))
final_cross_squared = np.zeros(len(final_cross_lags))

final_cross_numbers = np.zeros(len(final_cross_lags))
for i in range(len(cross_lags)):
    for k in range(len(cross_lags[i])):
        z = cross_lags[i][k] + 1000
        Z = cross[i][k]
        final_cross[z] += Z
        final_cross_squared[z] += Z**2
        final_cross_numbers[z] += 1

final_cross = final_cross/final_cross_numbers
final_cross_squared = final_cross_squared/final_cross_numbers

final_cross_error = np.sqrt( final_cross_squared - final_cross**2 )/2


plt.figure(figsize = (5,5))
plt.plot(final_cross_lags, final_cross)
plt.fill_between(final_cross_lags, final_cross - final_cross_error, final_cross + final_cross_error,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

plt.ylim([-0.55,0.5])
plt.xlim([-5,5])

plt.xlabel(r'$\tau$ (h)', fontsize = 14)
plt.ylabel(r'Cross-correlation $C_{gfp,g}(\tau)$', fontsize = 14)
plt.tight_layout()
