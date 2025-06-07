import numpy as np
import pickle
import random

#INPUT 
number_of_positions = 21
bin_time = 8 #8min in this experiment

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

for p in range(49, 49 + number_of_positions):
    
    pixels_cells_p = []
    cfp_cells_p = []
    yfp_cells_p = []
    rfp_cells_p = []
    frames_cells_p = []
    areas_cells_p = []
    lengths_cells_p = []
    growth_rate_cells_p = []
    growth_rate_smooth_cells_p = []
    
    with open('yfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_yfp_load = pickle.load(f)
        
    with open('cfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_cfp_load = pickle.load(f)
    
    with open('rfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_rfp_load = pickle.load(f)
        
    with open('lengths_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_lengths_load = pickle.load(f)
        
    with open('areas_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_areas_load = pickle.load(f)
        
    with open('frames_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_frames_load = pickle.load(f)
        
    with open('frames_purged_xpixels' +str(p) + '-purge2.pkl', 'rb') as f:
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
                    
                        
                            
                N = 10 #moving average
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


            pixels_cells.append(unique_cells[k])
            cfp_cells.append(np.array(cfp_temp))
            yfp_cells.append(np.array(yfp_temp))
            rfp_cells.append(np.array(rfp_temp))
            frames_cells.append(np.array(frames_temp))
            areas_cells.append(np.array(areas_temp))
            lengths_cells.append(np.array(lengths_temp))
            growth_rate_cells.append(np.array(growth_rate_temp))


                




#Loading cell data with lost plasmid:
pixels_cells_b = []
cfp_cells_b = []
yfp_cells_b = []
rfp_cells_b = []
frames_cells_b = []
areas_cells_b = []
lengths_cells_b = []
growth_rate_cells_b = []

for p in range(49, 49 + number_of_positions):
    
    pixels_cells_p = []
    cfp_cells_p = []
    yfp_cells_p = []
    rfp_cells_p = []
    frames_cells_p = []
    areas_cells_p = []
    lengths_cells_p = []
    growth_rate_cells_p = []
    growth_rate_smooth_cells_p = []
    
    with open('yfp_purged_pos' +str(p) + '-purge2_b.pkl', 'rb') as f:
        final_yfp_load = pickle.load(f)
        
    with open('cfp_purged_pos' +str(p) + '-purge2_b.pkl', 'rb') as f:
        final_cfp_load = pickle.load(f)
    
    with open('rfp_purged_pos' +str(p) + '-purge2_b.pkl', 'rb') as f:
        final_rfp_load = pickle.load(f)
        
    with open('lengths_purged_pos' +str(p) + '-purge2_b.pkl', 'rb') as f:
        final_lengths_load = pickle.load(f)
        
    with open('areas_purged_pos' +str(p) + '-purge2_b.pkl', 'rb') as f:
        final_areas_load = pickle.load(f)
        
    with open('frames_purged_pos' +str(p) + '-purge2_b.pkl', 'rb') as f:
        final_frames_load = pickle.load(f)
        
    with open('frames_purged_xpixels' +str(p) + '-purge2_b.pkl', 'rb') as f:
        final_xpixels_load = pickle.load(f)
            

        
    for cell in range(0,len(final_cfp_load)):        
        if len(final_lengths_load[cell]) > 0 :
            
            
            cell_length = final_lengths_load[cell]
            #Getting growth rates:
            division_times = []
            for i in range(len(final_lengths_load[cell])-1):
                if final_lengths_load[cell][i+1]  < 0.8*final_lengths_load[cell][i]:    #This finds the divisions
                    division_times.append(i+1)
                    
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
                    
                        
                            
        
                N = 10 #moving average
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


            pixels_cells_b.append(unique_cells[k])
            cfp_cells_b.append(np.array(cfp_temp))
            yfp_cells_b.append(np.array(yfp_temp))
            rfp_cells_b.append(np.array(rfp_temp))
            frames_cells_b.append(np.array(frames_temp))
            areas_cells_b.append(np.array(areas_temp))
            lengths_cells_b.append(np.array(lengths_temp))
            growth_rate_cells_b.append(np.array(growth_rate_temp))

    
    
number_of_cells = len(cfp_cells)
number_of_cells_b = len(cfp_cells_b)

cfp_avg_b = np.zeros(number_of_cells_b)
yfp_avg_b = np.zeros(number_of_cells_b)

for i in range(len(cfp_avg_b)):
    cfp_avg_b[i] = np.average(cfp_cells_b[i])
    yfp_avg_b[i] = np.average(yfp_cells_b[i])
    
min_cfp_b = np.min(cfp_avg_b)
min_yfp_b = np.min(yfp_avg_b)

for i in range(number_of_cells):
    for j in range(len(cfp_cells[i])):
        cfp_cells[i][j] = cfp_cells[i][j] 
        yfp_cells[i][j] = yfp_cells[i][j] 

        
for i in range(number_of_cells_b):
    for j in range(len(cfp_cells_b[i])):
        cfp_cells_b[i][j] = cfp_cells_b[i][j] 
        yfp_cells_b[i][j] = yfp_cells_b[i][j] 

#Number of samples for bootstrapping
number_of_samples = 10
sample_size = int(number_of_cells/number_of_samples)



etaxz_final = []
etayz_final = []
rhoxz_final = []
rhoyz_final = []
xbar_final  = []
ybar_final  = []
zbar_final  = []
etaxg_final = []
etayg_final = []
etaxl_final = []
etayl_final = []
rhoxg_final = []
rhoyg_final = []
rhoxl_final = []
rhoyl_final = []
gbar_final  = []
lbar_final  = []
cvz_final   = []
cvg_final   = []


max_frame = 180


mixed_cell_indices = np.array(range(0,len(rfp_cells)))
random.shuffle(mixed_cell_indices)

#Taking split samples of cell distribution
for sample in range(number_of_samples):
    cfp_sample = []
    yfp_sample = []
    rfp_sample = []
    pixels_sample = []
    frames_sample = []
    lengths_sample = []
    growth_rate_sample = []
    
    for cell in range(sample*sample_size, sample*sample_size + sample_size):
        cell_index = mixed_cell_indices[cell]
        for k in range(len(frames_cells[cell_index])):
            cfp_sample.append(cfp_cells[cell_index][k])
            yfp_sample.append(yfp_cells[cell_index][k])
            rfp_sample.append(rfp_cells[cell_index][k])
            pixels_sample.append(pixels_cells[cell_index])
            frames_sample.append(frames_cells[cell_index][k])
            lengths_sample.append(lengths_cells[cell_index][k])
            growth_rate_sample.append(growth_rate_cells[cell_index][k])
    
    cfp_sample_b = []
    yfp_sample_b = []
    rfp_sample_b = []
    pixels_sample_b = []
    frames_sample_b = []
    lengths_sample_b = []
    growth_rate_sample_b = []
    
    
    sample_size_b = int(number_of_cells_b/number_of_samples)
    mixed_cell_indices_b = np.array(range(0,len(rfp_cells_b)))
    random.shuffle(mixed_cell_indices_b)


    for cell in range(sample*sample_size_b, sample*sample_size_b + sample_size_b):
        random_cell_b = mixed_cell_indices_b[cell]
        for k in range(len(frames_cells_b[random_cell_b])):
            cfp_sample_b.append(cfp_cells_b[random_cell_b][k])
            yfp_sample_b.append(yfp_cells_b[random_cell_b][k])
            rfp_sample_b.append(rfp_cells_b[random_cell_b][k])
            pixels_sample_b.append(pixels_cells_b[random_cell_b])
            frames_sample_b.append(frames_cells_b[random_cell_b][k])
            lengths_sample_b.append(lengths_cells_b[random_cell_b][k])
            growth_rate_sample_b.append(growth_rate_cells_b[random_cell_b][k])
        
    #Turning sample data sets into arrays for lost plasmid
    pixels_sample_b = np.array(pixels_sample_b)
    cfp_sample_b = np.array(cfp_sample_b)
    yfp_sample_b = np.array(yfp_sample_b)
    growth_rate_sample_b = np.array(growth_rate_sample_b)
    lengths_sample_b = np.array(lengths_sample_b)
    rfp_sample_b = np.array(rfp_sample_b)
    frames_sample_b = np.array(frames_sample_b)
    growth_rate_sample_b = np.array(growth_rate_sample_b)
    
    #### DRIFT CORRECTION ###
    number_of_frames = max_frame #Set this to the length of the time trafes
    cfp_time_bins = np.zeros(number_of_frames)
    cfp_time_bins_num = np.zeros(number_of_frames)
    for i in range(len(frames_sample)):
        if frames_sample[i] < number_of_frames :
            cfp_time_bins[int(frames_sample[i])] = cfp_time_bins[int(frames_sample[i])] + cfp_sample[i]
            cfp_time_bins_num[int(frames_sample[i])] = cfp_time_bins_num[int(frames_sample[i])] + 1
    cfp_time_bins = cfp_time_bins/cfp_time_bins_num


    yfp_time_bins = np.zeros(number_of_frames)
    yfp_time_bins_num = np.zeros(number_of_frames)
    for i in range(len(frames_sample)):
        if frames_sample[i] < number_of_frames :
            yfp_time_bins[int(frames_sample[i])] = yfp_time_bins[int(frames_sample[i])] + yfp_sample[i]
            yfp_time_bins_num[int(frames_sample[i])] = yfp_time_bins_num[int(frames_sample[i])] + 1
    yfp_time_bins = yfp_time_bins/yfp_time_bins_num


    rfp_time_bins = np.zeros(number_of_frames)
    rfp_time_bins_num = np.zeros(number_of_frames)
    for i in range(len(frames_sample)):
        if frames_sample[i] < number_of_frames :
            rfp_time_bins[int(frames_sample[i])] = rfp_time_bins[int(frames_sample[i])] + rfp_sample[i]
            rfp_time_bins_num[int(frames_sample[i])] = rfp_time_bins_num[int(frames_sample[i])] + 1
    rfp_time_bins = rfp_time_bins/rfp_time_bins_num

    
    #In the following, 50 is set at the initial time trace cut off due to photobleaching.
    #Correcting the time-drift:
    Z = np.polyfit(np.array(range(50, len(rfp_time_bins))), rfp_time_bins[50:], 2)
    P = np.poly1d(Z)

    for i in range(len(rfp_sample)):
        if frames_sample[i] < number_of_frames :
            rfp_sample[i] = rfp_sample[i]/P(int(frames_sample[i]))*P(50)

    for i in range(len(rfp_sample_b)):
        rfp_sample_b[i] = rfp_sample_b[i]/P(int(frames_sample_b[i]))*P(50)
        
    Z = np.polyfit(np.array(range(50, len(yfp_time_bins))), yfp_time_bins[50:], 2)
    P = np.poly1d(Z)

    for i in range(len(yfp_sample)):
        if frames_sample[i] < number_of_frames :
            yfp_sample[i] = yfp_sample[i]/P(int(frames_sample[i]))*P(50)
            
    for i in range(len(yfp_sample_b)):
        yfp_sample_b[i] = yfp_sample_b[i]/P(int(frames_sample_b[i]))*P(50)
        
    Z = np.polyfit(np.array(range(50, len(cfp_time_bins))), cfp_time_bins[50:], 2)
    P = np.poly1d(Z)

    for i in range(len(cfp_sample)):
            if frames_sample[i] < number_of_frames :
                cfp_sample[i] = cfp_sample[i]/P(int(frames_sample[i]))*P(50)

    for i in range(len(cfp_sample_b)):
        cfp_sample_b[i] = cfp_sample_b[i]/P(int(frames_sample_b[i]))*P(50)

    
    #######  Non-even illumination correction    #######
    bsize = 100 
    number_of_bins = int(2050/bsize)

    pixel_bins = []
    cfp_bins = []
    yfp_bins = []
    rfp_bins = []
    
    for i in range(number_of_bins):
        cfp_average = 0
        yfp_average = 0
        rfp_average = 0
        
        number = 0
        for j in range(len(pixels_sample)):
            if i*bsize <= pixels_sample[j] < (i+1)*bsize:
                if frames_sample[j] > 50:
                    cfp_average = cfp_average + cfp_sample[j] 
                    yfp_average = yfp_average + yfp_sample[j]
                    rfp_average = rfp_average + rfp_sample[j]
                    
                    number = number + 1
        if number > 0 :
            #print(number)
            cfp_average = cfp_average/number
            cfp_bins.append(cfp_average)
            
            
            yfp_average = yfp_average/number
            yfp_bins.append(yfp_average)
            
            rfp_average = rfp_average/number
            rfp_bins.append(rfp_average)

            pixel_bins.append((i+0.5)*bsize)
            
    z_cfp = np.polyfit(pixel_bins, cfp_bins, 3)
    z_yfp = np.polyfit(pixel_bins, yfp_bins, 3)
    z_rfp = np.polyfit(pixel_bins, rfp_bins, 3)





    pix = np.linspace(0,2000, 2000)
    
    #These are the curves used to correct for the non-even illumination

    P_cfp = np.poly1d(z_cfp)
    z_cfp_max = np.max(P_cfp(pix))
    

    P_yfp = np.poly1d(z_yfp)
    z_yfp_max = np.max(P_yfp(pix))
    

    P_rfp = np.poly1d(z_rfp)
    z_rfp_max = np.max(P_rfp(pix))

    

###   Getting autofluorescence    ###

    cfp_average_b = 0
    yfp_average_b = 0
    rfp_average_b = 0 
    growth_rate_average_b = 0
    lengths_average_b = 0
    xx_bins_b = 0
    yy_bins_b = 0
    xz_bins_b = 0
    yz_bins_b = 0    
    xg_bins_b = 0
    yg_bins_b = 0
    xl_bins_b = 0
    yl_bins_b = 0
    covxz_b = 0
    covyz_b = 0
    covxg_b = 0
    covyg_b = 0
    covxl_b = 0
    covyl_b = 0
    number_b = 0
    
    
    for i in range(len(pixels_sample_b)):

        
        if frames_sample_b[i] > 50 and frames_sample_b[i] < max_frame:
            cfp_average_b = cfp_average_b + cfp_sample_b[i]/P_cfp(pixels_sample_b[i])*z_cfp_max
            yfp_average_b = yfp_average_b + yfp_sample_b[i]/P_yfp(pixels_sample_b[i])*z_yfp_max
            rfp_average_b = rfp_average_b + rfp_sample_b[i]/P_rfp(pixels_sample_b[i])*z_rfp_max
            
            growth_rate_average_b = growth_rate_average_b + growth_rate_sample_b[i]
            lengths_average_b = lengths_average_b + lengths_sample_b[i]
            
            yy_bins_b = yy_bins_b + cfp_sample_b[i]*cfp_sample_b[i]/P_cfp(pixels_sample_b[i])*z_cfp_max/P_cfp(pixels_sample_b[i])*z_cfp_max
            xx_bins_b = xx_bins_b + yfp_sample_b[i]*yfp_sample_b[i]/P_yfp(pixels_sample_b[i])*z_yfp_max/P_yfp(pixels_sample_b[i])*z_yfp_max

            yz_bins_b = yz_bins_b + cfp_sample_b[i]*rfp_sample_b[i]/P_rfp(pixels_sample_b[i])*z_rfp_max/P_cfp(pixels_sample_b[i])*z_cfp_max
            xz_bins_b = xz_bins_b + yfp_sample_b[i]*rfp_sample_b[i]/P_rfp(pixels_sample_b[i])*z_rfp_max/P_yfp(pixels_sample_b[i])*z_yfp_max

            yg_bins_b = yg_bins_b + cfp_sample_b[i]*growth_rate_sample_b[i]/P_cfp(pixels_sample_b[i])*z_cfp_max
            xg_bins_b = xg_bins_b + yfp_sample_b[i]*growth_rate_sample_b[i]/P_yfp(pixels_sample_b[i])*z_yfp_max

            yl_bins_b = yl_bins_b + cfp_sample_b[i]*lengths_sample_b[i]/P_cfp(pixels_sample_b[i])*z_cfp_max
            xl_bins_b = xl_bins_b + yfp_sample_b[i]*lengths_sample_b[i]/P_yfp(pixels_sample_b[i])*z_yfp_max
        
            number_b = number_b + 1
            
            
    if number_b > 0 :
        cfp_average_b = cfp_average_b/number_b
        yfp_average_b = yfp_average_b/number_b
        rfp_average_b = rfp_average_b/number_b
        
        growth_rate_average_b = growth_rate_average_b/number_b
        lengths_average_b = lengths_average_b/number_b
        
        yy_bins_b = yy_bins_b/number_b
        xx_bins_b = xx_bins_b/number_b
        
        yz_bins_b = yz_bins_b/number_b
        xz_bins_b = xz_bins_b/number_b
        
        yg_bins_b = yg_bins_b/number_b
        xg_bins_b = xg_bins_b/number_b
        yl_bins_b = yl_bins_b/number_b
        xl_bins_b = xl_bins_b/number_b  
        
        vary_b = yy_bins_b - cfp_average_b**2
        varx_b = xx_bins_b - yfp_average_b**2

        covyz_b = yz_bins_b - cfp_average_b*rfp_average_b
        covxz_b = xz_bins_b - yfp_average_b*rfp_average_b
        
        covyg_b = yg_bins_b - cfp_average_b*growth_rate_average_b
        covxg_b = xg_bins_b - yfp_average_b*growth_rate_average_b
        
        covyl_b = yl_bins_b - cfp_average_b*lengths_average_b
        covxl_b = xl_bins_b - yfp_average_b*lengths_average_b
        
        

### CALCULATING ETAS ###

        cfp_average = 0
        yfp_average = 0
        rfp_average = 0
        
        growth_rate_average = 0
        lengths_average = 0
        
        xz_bins = 0
        yz_bins = 0
        
        xg_bins = 0
        yg_bins = 0
        xl_bins = 0
        yl_bins = 0
        
        xx_bins = 0 
        yy_bins = 0
        zz_bins = 0
        gg_bins = 0
        ll_bins = 0
        
        xy_bins = 0
        
        number = 0
        for i in range(len(pixels_sample)):
    
            
            if frames_sample[i] > 50 and frames_sample[i] < max_frame:
                cfp_average = cfp_average + cfp_sample[i]/P_cfp(pixels_sample[i])*z_cfp_max
                yfp_average = yfp_average + yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max
                rfp_average = rfp_average + rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max
                
                growth_rate_average = growth_rate_average + growth_rate_sample[i]
                lengths_average = lengths_average + lengths_sample[i]
                
                yz_bins = yz_bins + cfp_sample[i]*rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max/P_cfp(pixels_sample[i])*z_cfp_max
                xz_bins = xz_bins + yfp_sample[i]*rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max/P_yfp(pixels_sample[i])*z_yfp_max
                        
                yg_bins = yg_bins + growth_rate_sample[i]*cfp_sample[i]/P_cfp(pixels_sample[i])*z_cfp_max
                xg_bins = xg_bins + growth_rate_sample[i]*yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max
                
                yl_bins = yl_bins + lengths_sample[i]*cfp_sample[i]/P_cfp(pixels_sample[i])*z_cfp_max
                xl_bins = xl_bins + lengths_sample[i]*yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max
    
                yy_bins = yy_bins + cfp_sample[i]*cfp_sample[i]/P_cfp(pixels_sample[i])*z_cfp_max/P_cfp(pixels_sample[i])*z_cfp_max
                xx_bins = xx_bins + yfp_sample[i]*yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max/P_yfp(pixels_sample[i])*z_yfp_max
                zz_bins = zz_bins + rfp_sample[i]*rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max/P_rfp(pixels_sample[i])*z_rfp_max
            
                gg_bins = gg_bins + growth_rate_sample[i]*growth_rate_sample[i]
                ll_bins = ll_bins + lengths_sample[i]*lengths_sample[i]
            
                xy_bins = xy_bins + cfp_sample[i]*yfp_sample[i]/P_cfp(pixels_sample[i])*z_cfp_max/P_yfp(pixels_sample[i])*z_yfp_max
                
                number = number + 1
            
        if number > 0 :
            #print(number)
        
            
            cfp_average = cfp_average/number
            #Correcting the autofluorescnece/background:
            cfp_average_2 = cfp_average - (cfp_average_b)
                
                
            yfp_average = yfp_average/number
            #Correcting the autofluorescnece/background:
            yfp_average_2 = yfp_average - (yfp_average_b )
                
            rfp_average = rfp_average/number
                
            growth_rate_average = growth_rate_average/number
            lengths_average = lengths_average/number
                
            xz_bins = xz_bins/number
            yz_bins = yz_bins/number
            
            xg_bins = xg_bins/number
            yg_bins = yg_bins/number
            xl_bins = xl_bins/number
            yl_bins = yl_bins/number
            
            xx_bins = xx_bins/number
            yy_bins = yy_bins/number
            zz_bins = zz_bins/number
            
            gg_bins = gg_bins/number
            ll_bins = ll_bins/number
                
            xy_bins = xy_bins/number
            
            covyz = (yz_bins - cfp_average*rfp_average)
            covxz = (xz_bins - yfp_average*rfp_average)
            
            covyg = (yg_bins - cfp_average*growth_rate_average)
            covxg = (xg_bins - yfp_average*growth_rate_average)
            covyl = (yl_bins - cfp_average*lengths_average)
            covxl = (xl_bins - yfp_average*lengths_average)
            
            vary = (yy_bins - cfp_average**2)
            varx = (xx_bins - yfp_average**2)
            varz = (zz_bins - rfp_average**2)
            
            varg = (gg_bins - growth_rate_average**2)
            varl = (ll_bins - lengths_average**2)
            
            vary_2 = vary 
            varx_2 = varx 
            
            
            #Correcting for background/autofluorescence covariance:
            covxz_2 = covxz 
            covyz_2 = covyz 
            
            covxl_2 = covxl 
            covyl_2 = covyl
            
            covxg_2 = covxg 
            covyg_2 = covyg 
            
            #Final etas:
            etayz = covyz_2/cfp_average_2/rfp_average
            etaxz = covxz_2/yfp_average_2/rfp_average
            
            etayg = covyg_2/cfp_average_2/growth_rate_average
            etaxg = covxg_2/yfp_average_2/growth_rate_average
            etayl = covyl_2/cfp_average_2/lengths_average
            etaxl = covxl_2/yfp_average_2/lengths_average
            
            
            rhoxz = covxz_2/np.sqrt(varx_2*varz)
            rhoyz = covyz_2/np.sqrt(vary_2*varz)
            
            rhoxg = covxg_2/np.sqrt(varx_2*varg)
            rhoyg = covyg_2/np.sqrt(vary_2*varg)
            rhoxl = covxl_2/np.sqrt(varx_2*varl)
            rhoyl = covyl_2/np.sqrt(vary_2*varl)
            
            cvz = np.sqrt(varz/rfp_average/rfp_average)
            cvg = np.sqrt(varg/growth_rate_average/growth_rate_average)
                        
            etaxz_final.append(etaxz)
            etayz_final.append(etayz)
                
            etaxg_final.append(etaxg)
            etayg_final.append(etayg)
                
            rhoxz_final.append(rhoxz)
            rhoyz_final.append(rhoyz)
                
            rhoxg_final.append(rhoxg)
            rhoyg_final.append(rhoyg)
                
            etaxl_final.append(etaxl)
            etayl_final.append(etayl)
            rhoxl_final.append(rhoxl)
            rhoyl_final.append(rhoyl)
                
            xbar_final.append(cfp_average_2)
            ybar_final.append(yfp_average_2)
            zbar_final.append(rfp_average)
                
            gbar_final.append(growth_rate_average)
            lbar_final.append(lengths_average)
                
            cvz_final.append(cvz)
            cvg_final.append(cvg)
  
            print(sample)                        

cvz_final = np.array(cvz_final)
cvg_final = np.array(cvg_final)

CVZ = np.average(cvz_final)
CVZ_ERR = np.std(cvz_final)*2

CVG = np.average(cvg_final)
CVG_ERR = np.std(cvg_final)*2


etaxz_final = np.array(etaxz_final)
etayz_final = np.array(etayz_final)
rhoxz_final = np.array(rhoxz_final)
rhoyz_final = np.array(rhoyz_final)

etaxg_final = np.array(etaxg_final)
etayg_final = np.array(etayg_final)
rhoxg_final = np.array(rhoxg_final)
rhoyg_final = np.array(rhoyg_final)

etaxl_final = np.array(etaxl_final)
etayl_final = np.array(etayl_final)
rhoxl_final = np.array(rhoxl_final)
rhoyl_final = np.array(rhoyl_final)

ETAXZ = np.average(etaxz_final)
ETAXZ_ERR = np.std(etaxz_final)*2/np.sqrt(number_of_samples-1)#/np.sqrt(number_of_samples-1)
ETAYZ = np.average(etayz_final)
ETAYZ_ERR = np.std(etayz_final)*2/np.sqrt(number_of_samples-1)#/np.sqrt(number_of_samples-1)
RHOXZ = np.average(rhoxz_final)
RHOXZ_ERR = np.std(rhoxz_final)*2/np.sqrt(number_of_samples-1)
RHOYZ = np.average(rhoyz_final)
RHOYZ_ERR = np.std(rhoyz_final)*2/np.sqrt(number_of_samples-1)
XBAR = np.average(xbar_final)
XBAR_ERR = np.std(xbar_final)*2/np.sqrt(number_of_samples-1)
YBAR = np.average(ybar_final)
YBAR_ERR = np.std(ybar_final)*2/np.sqrt(number_of_samples-1)

ZBAR = np.average(zbar_final)
ZBAR_ERR = np.std(zbar_final)*2/np.sqrt(number_of_samples-1)


ETAXG = np.average(etaxg_final)
ETAXG_ERR = np.std(etaxg_final)*2/np.sqrt(number_of_samples-1)#/np.sqrt(number_of_samples-1)
ETAYG = np.average(etayg_final)
ETAYG_ERR = np.std(etayg_final)*2/np.sqrt(number_of_samples-1)#/np.sqrt(number_of_samples-1)
RHOXG = np.average(rhoxg_final)
RHOXG_ERR = np.std(rhoxg_final)*2/np.sqrt(number_of_samples-1)
RHOYG = np.average(rhoyg_final)
RHOYG_ERR = np.std(rhoyg_final)*2/np.sqrt(number_of_samples-1)
GBAR = np.average(gbar_final)
GBAR_ERR = np.std(gbar_final)*2/np.sqrt(number_of_samples-1)

ETAXL = np.average(etaxl_final)
ETAXL_ERR = np.std(etaxl_final)*2/np.sqrt(number_of_samples-1)#/np.sqrt(number_of_samples-1)
ETAYL = np.average(etayl_final)
ETAYL_ERR = np.std(etayl_final)*2/np.sqrt(number_of_samples-1)#/np.sqrt(number_of_samples-1)
RHOXL = np.average(rhoxl_final)
RHOXL_ERR = np.std(rhoxl_final)*2/np.sqrt(number_of_samples-1)
RHOYL = np.average(rhoyl_final)
RHOYL_ERR = np.std(rhoyl_final)*2/np.sqrt(number_of_samples-1)
LBAR = np.average(lbar_final)
LBAR_ERR = np.std(lbar_final)*2/np.sqrt(number_of_samples-1)


GENERATION_TIME = np.average(time_to_divide)*8



final_data = {'etaxz': ETAXZ, 'etaxz_err': ETAXZ_ERR, 'etayz': ETAYZ, 'etayz_err': ETAYZ_ERR, \
              'etaxg': ETAXG, 'etaxg_err': ETAXG_ERR, 'etayg': ETAYG, 'etayg_err': ETAYG_ERR, \
              'etaxa': ETAXL, 'etaxa_err': ETAXL_ERR, 'etaya': ETAYL, 'etaya_err': ETAYL_ERR, \
              'rhoxz': RHOXZ, 'rhoxz_err': RHOXZ_ERR, 'rhoyz': RHOYZ, 'rhoyz_err': RHOYZ_ERR, \
              'rhoxg': RHOXG, 'rhoxg_err': RHOXG_ERR, 'rhoyg': RHOYG, 'rhoyg_err': RHOYG_ERR, \
              'rhoxa': RHOXL, 'rhoxa_err': RHOXL_ERR, 'rhoya': RHOYL, 'rhoya_err': RHOYL_ERR, \
              'xavg' : XBAR,  'xavg_err' : XBAR_ERR,  'yavg' : YBAR,  'yavg_err' : YBAR_ERR,  \
              'l_avg': LBAR,  'l_avg_err': LBAR_ERR,  'growth_rate_avg': GBAR, 'growth_rate_avg_err': GBAR_ERR, \
              'generation_time': GENERATION_TIME}
    
    
with open('final_statistics/PA52_2uMIPTG_split.pkl', 'wb') as f:
    pickle.dump(final_data, f)


