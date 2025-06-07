import matplotlib.pyplot as plt
import numpy as np
import pickle
from scipy import signal



#INPUT 
number_of_positions = 10
bin_time = 5 

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
cross = []
cross_lags = []
path = '../data/delta/EJS2/'

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
    
    with open(path + 'yfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_yfp_load = pickle.load(f)
        
    with open(path + 'cfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_cfp_load = pickle.load(f)
    
    with open(path + 'rfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_rfp_load = pickle.load(f)
        
    with open(path + 'lengths_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_lengths_load = pickle.load(f)
        
    with open(path + 'areas_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_areas_load = pickle.load(f)
        
    with open(path + 'frames_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_frames_load = pickle.load(f)
        
    with open(path + 'frames_purged_xpixels' +str(p) + '-purge2.pkl', 'rb') as f:
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
                    
        
                growth_rate_cells_p.append(np.array(temp_growth_rates)/bin_time)
                    
           
            
    if len(pixels_cells_p) > 0 : 
        
        #growth_rate_smooth_temp = []
        
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
            frames_cells.append(np.array(frames_temp))
            areas_cells.append(np.array(areas_temp))
            lengths_cells.append(np.array(lengths_temp))
            rfp_rate_temp = []
            for _ in range(len(rfp_temp)):
                
                if _ == 0:
                    rate = (rfp_temp[1] - rfp_temp[0])/bin_time
                elif _ < len(rfp_temp) - 1 :
                    rate = (rfp_temp[_+1] - rfp_temp[_-1])/2/bin_time
                else:
                    rate = (rfp_temp[-1] - rfp_temp[-2])/1/bin_time
                rfp_rate_temp.append(rate)
    
            M = 5 #moving average
            
            temp_cfp_smooth = np.convolve( cfp_temp, np.ones(M)/M, mode='valid')
            
            cfp_cells.append(np.array(temp_cfp_smooth))
            
            temp_yfp_smooth = np.convolve( yfp_temp, np.ones(M)/M, mode='valid')
            
            yfp_cells.append(np.array(temp_yfp_smooth))

            temp_growth_rates_smooth = np.convolve( growth_rate_temp, np.ones(M)/M, mode='valid')
            
            growth_rate_cells.append(np.array(growth_rate_temp))

            temp_rfp_rate_smooth = np.convolve( rfp_rate_temp, np.ones(M)/M, mode='valid')
            temp_rfp_smooth = np.convolve( rfp_temp, np.ones(M)/M, mode='valid')

            rfp_cells.append(np.array(   rfp_temp     )  )

    
    
number_of_cells = len(cfp_cells)


#Number of samples for bootstrapping
number_of_samples = 1



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



max_frame = 145
min_frame = 60


#Taking bootstrapping samples of cell distribution
for sample in range(number_of_samples):
    cfp_sample = []
    yfp_sample = []
    rfp_sample = []
    pixels_sample = []
    frames_sample = []
    lengths_sample = []
    growth_rate_sample = []
    
    for cell in range(number_of_cells):
        random_cell = cell
        for k in range(len(cfp_cells[random_cell])):
            if frames_cells[random_cell][k] > min_frame and frames_cells[random_cell][k] < max_frame:
                cfp_sample.append(cfp_cells[random_cell][k])
                yfp_sample.append(yfp_cells[random_cell][k])
                rfp_sample.append(rfp_cells[random_cell][k])
                pixels_sample.append(pixels_cells[random_cell])
                frames_sample.append(frames_cells[random_cell][k])
                lengths_sample.append(lengths_cells[random_cell][k])
                growth_rate_sample.append(growth_rate_cells[random_cell][k])
         
    #Turning sample data sets into arrays
    pixels_sample = np.array(pixels_sample)
    cfp_sample = np.array(cfp_sample)
    yfp_sample = np.array(yfp_sample)
    growth_rate_sample = np.array(growth_rate_sample)
    lengths_sample = np.array(lengths_sample)
    rfp_sample = np.array(rfp_sample)
    frames_sample = np.array(frames_sample)    
    
    
    
    
    
    #### DRIFT CORRECTION ###
    number_of_frames = max_frame   #Set this to the length of the time trafes
    cfp_time_bins = np.zeros(number_of_frames)
    cfp_time_bins_num = np.zeros(number_of_frames)
    for i in range(len(frames_sample)):
        if frames_sample[i] < max_frame :
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
    Z = np.polyfit(np.array(range(min_frame + 1 , len(rfp_time_bins))), rfp_time_bins[min_frame + 1:], 2)
    P = np.poly1d(Z)

    for i in range(len(rfp_sample)):
        if frames_sample[i] < number_of_frames :
            rfp_sample[i] = rfp_sample[i]/P(int(frames_sample[i]))*P(0)

        
    for cell in range(len(rfp_cells)):
        for i in range(len(rfp_cells[cell])):
            rfp_cells[cell][i] = rfp_cells[cell][i]/P(int(frames_cells[cell][i]))*P(0)

        
    Z = np.polyfit(np.array(range(min_frame + 1, len(yfp_time_bins))), yfp_time_bins[min_frame + 1:], 2)
    P = np.poly1d(Z)

    for i in range(len(yfp_sample)):
        if frames_sample[i] < number_of_frames :
            yfp_sample[i] = yfp_sample[i]/P(int(frames_sample[i]))*P(0)
            
        
    Z = np.polyfit(np.array(range( min_frame + 1, len(cfp_time_bins))), cfp_time_bins[min_frame + 1:], 2)
    P = np.poly1d(Z)

    for i in range(len(cfp_sample)):
            if frames_sample[i] < number_of_frames :
                cfp_sample[i] = cfp_sample[i]/P(int(frames_sample[i]))*P(0)

    
    #######  Non-even illumination correction    #######
    bsize = 50 
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
                if frames_sample[j] > min_frame and frames_sample[j] < max_frame:
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

    

    for cell in range(len(rfp_cells)):
        for i in range(len(rfp_cells[cell])):
            rfp_cells[cell][i] = rfp_cells[cell][i]/P_rfp(pixels_sample[i])*z_rfp_max
    
            
                
            
 
cross = []
cross_lags = []

for cell in range(len(rfp_cells)):
    rfp_temp = rfp_cells[cell]
    growth_rate_temp = growth_rate_cells[cell]

    
    M = 5 #moving average
        
    
    growth_rate_temp = np.convolve( growth_rate_temp, np.ones(M)/M, mode='same')

    corr = signal.correlate( (rfp_temp - np.average(rfp_temp)), (growth_rate_temp - np.average(growth_rate_temp)), mode = 'full') 
    cross_corr1 = np.sum((rfp_temp - np.average(rfp_temp))**2)
    cross_corr2 =  np.sum((growth_rate_temp - np.average(growth_rate_temp))**2)

    lags = signal.correlation_lags(len(rfp_temp), len(rfp_temp))
    ww = np.where(lags == 0)[0]
    corr /= np.sqrt(cross_corr1*cross_corr2)
    cross.append( corr )
    cross_lags.append(lags)

final_cross_lags = np.array(range(-510,510))*5./60
final_cross = np.zeros(len(final_cross_lags))
final_cross_squared = np.zeros(len(final_cross_lags))

final_cross_numbers = np.zeros(len(final_cross_lags))
for i in range(len(cross_lags)):
    for k in range(len(cross_lags[i])):
        z = cross_lags[i][k] + 510
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
plt.ylabel(r'Cross-correlation $C_{rfp,g}(\tau)$', fontsize = 14)
plt.tight_layout()




