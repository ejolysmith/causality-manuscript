import numpy as np
import pickle
import random


#INPUT 
number_of_positions = 20
bin_time = 5 #8min

pixels_cells = []
gfp_cells = []
#yfp_cells = []
rfp_cells = []
frames_cells = []
areas_cells = []
lengths_cells = []
growth_rate_cells = []
growth_rate_smooth_cells = []

time_to_divide = []

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
        
    with open('gfp_purged_pos' +str(p) + '-purge2.pkl', 'rb') as f:
        final_gfp_load = pickle.load(f)
    
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
                    
                        
                            
                N = 10 #moving average
                temp_growth_rates_smooth = np.convolve(temp_growth_rates, np.ones(N)/N, mode='valid')/bin_time
                growth_rate_smooth_cells_p.append(temp_growth_rates_smooth)
                growth_rate_cells_p.append(np.array(temp_growth_rates)/bin_time)
                    
           
            
    if len(pixels_cells_p) > 0 : 
        
        #growth_rate_smooth_temp = []
        
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
                
                for kkk in range(len(  gfp_cells_p[cell_index]  ) ):
                    gfp_temp.append(gfp_cells_p[cell_index][kkk])
                    #yfp_temp.append(yfp_cells_p[cell_index][kkk])
                    rfp_temp.append(rfp_cells_p[cell_index][kkk])
                    frames_temp.append(frames_cells_p[cell_index][kkk])
                    areas_temp.append(areas_cells_p[cell_index][kkk])
                    lengths_temp.append(lengths_cells_p[cell_index][kkk])
                    growth_rate_temp.append(growth_rate_cells_p[cell_index][kkk])
                    #growth_rate_smooth_temp.append(growth_rate_smooth_cells_p[cell_index][kkk])

            pixels_cells.append(unique_cells[k])
            gfp_cells.append(np.array(gfp_temp))
            #yfp_cells.append(np.array(yfp_temp))
            rfp_cells.append(np.array(rfp_temp))
            frames_cells.append(np.array(frames_temp))
            areas_cells.append(np.array(areas_temp))
            lengths_cells.append(np.array(lengths_temp))
            growth_rate_cells.append(np.array(growth_rate_temp))
            #growth_rate_smooth_cells.append(growth_rate_smooth_temp)

                




#Loading cell data with lost plasmid:
pixels_cells_b = []
cfp_cells_b = []
yfp_cells_b = []
rfp_cells_b = []
frames_cells_b = []
areas_cells_b = []
lengths_cells_b = []
growth_rate_cells_b = []


number_of_cells = len(gfp_cells)
#number_of_cells_b = len(gfp_cells_b)


#Number of samples for bootstrapping
number_of_samples = 10
#sample_size = int(len(rfp)/number_of_samples)



etaxz_final = []
etayz_final = []
rhoxz_final = []
rhoyz_final = []
xbar_final  = []
ybar_final  = []
etaxg_final = []
etayg_final = []
etaxa_final = []
etaya_final = []
rhoxg_final = []
rhoyg_final = []
rhoxa_final = []
rhoya_final = []
gbar_final  = []
abar_final  = []
cvz_final = []
cvg_final = []
zbar_final = []

#random.shuffle(random_index)


max_frame = 400
min_frame = 50


#Taking bootstrapping samples of cell distribution
for sample in range(number_of_samples):
    gfp_sample = []
    #yfp_sample = []
    rfp_sample = []
    pixels_sample = []
    frames_sample = []
    lengths_sample = []
    growth_rate_sample = []
    
    for cell in range(number_of_cells):
        random_cell = random.randint(0, number_of_cells-1)
        for k in range(len(frames_cells[random_cell])):
            gfp_sample.append(gfp_cells[random_cell][k])
            #yfp_sample.append(yfp_cells[random_cell][k])
            rfp_sample.append(rfp_cells[random_cell][k])
            pixels_sample.append(pixels_cells[random_cell])
            frames_sample.append(frames_cells[random_cell][k])
            lengths_sample.append(lengths_cells[random_cell][k])
            growth_rate_sample.append(growth_rate_cells[random_cell][k])
     
    #Turning sample data sets into arrays
    pixels_sample = np.array(pixels_sample)
    gfp_sample = np.array(gfp_sample)
    growth_rate_sample = np.array(growth_rate_sample)
    lengths_sample = np.array(lengths_sample)
    rfp_sample = np.array(rfp_sample)
    frames_sample = np.array(frames_sample)    
    
    
    #### DRIFT CORRECTION ###
    number_of_frames = max_frame   #Set this to the length of the time trafes
    gfp_time_bins = np.zeros(number_of_frames)
    gfp_time_bins_num = np.zeros(number_of_frames)
    for i in range(len(frames_sample)):
        if frames_sample[i] < max_frame :
            gfp_time_bins[int(frames_sample[i])] = gfp_time_bins[int(frames_sample[i])] + gfp_sample[i]
            gfp_time_bins_num[int(frames_sample[i])] = gfp_time_bins_num[int(frames_sample[i])] + 1
    gfp_time_bins = gfp_time_bins/gfp_time_bins_num



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

    
        
    Z = np.polyfit(np.array(range( min_frame + 1, len(gfp_time_bins))), gfp_time_bins[min_frame + 1:], 2)
    P = np.poly1d(Z)

    for i in range(len(gfp_sample)):
            if frames_sample[i] < number_of_frames :
                gfp_sample[i] = gfp_sample[i]/P(int(frames_sample[i]))*P(0)

    
    
    #######  Non-even illumination correction    #######
    bsize = 100 #Do we need bins? 
    number_of_bins = int(2050/bsize)

    pixel_bins = []
    gfp_bins = []
    rfp_bins = []
    
    for i in range(number_of_bins):
        gfp_average = 0
        rfp_average = 0
        
        number = 0
        for j in range(len(pixels_sample)):
            if i*bsize <= pixels_sample[j] < (i+1)*bsize:
                if frames_sample[j] > min_frame and frames_sample[j] < max_frame:
                    gfp_average = gfp_average + gfp_sample[j]#/P_cfp((i+0.5)*bsize)*z_cfp_max
                    #yfp_average = yfp_average + yfp_sample[j]#/P_yfp((i+0.5)*bsize)*z_yfp_max
                    rfp_average = rfp_average + rfp_sample[j]
                    
                    number = number + 1
        if number > 0 :
            #print(number)
            gfp_average = gfp_average/number
            gfp_bins.append(gfp_average)
            
            
            
            rfp_average = rfp_average/number
            rfp_bins.append(rfp_average)

            pixel_bins.append((i+0.5)*bsize)
            
    z_gfp = np.polyfit(pixel_bins, gfp_bins, 3)
    #z_yfp = np.polyfit(pixel_bins, yfp_bins, 3)
    z_rfp = np.polyfit(pixel_bins, rfp_bins, 3)





    pix = np.linspace(0,2000, 2000)
    
    #These are the curves used to correct for the non-even illumination
    
    P_gfp = np.poly1d(z_gfp)
    z_gfp_max = np.max(P_gfp(pix))
    
    P_rfp = np.poly1d(z_rfp)
    z_rfp_max = np.max(P_rfp(pix))

    

    if 1 > 0 :
        
        
        
    
### CALCULATING ETAS ###

        gfp_average = 0
        #yfp_average = 0
        rfp_average = 0
        
        growth_rate_average = 0
        lengths_average = 0
        
        xz_bins = 0
        yz_bins = 0
        
        xg_bins = 0
        yg_bins = 0
        xa_bins = 0
        ya_bins = 0
        
        xx_bins = 0 
        yy_bins = 0
        zz_bins = 0
        gg_bins = 0
        aa_bins = 0
        
        xy_bins = 0
        
        number = 0
        for i in range(len(pixels_sample)):
    
            
            if frames_sample[i] > min_frame and frames_sample[i] < max_frame:
                
                gfp_average = gfp_average + gfp_sample[i]/P_gfp(pixels_sample[i])*z_gfp_max
                #yfp_average = yfp_average + yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max
                rfp_average = rfp_average + rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max
                
                growth_rate_average = growth_rate_average + growth_rate_sample[i]
                lengths_average = lengths_average + lengths_sample[i]
                
                xz_bins = xz_bins + gfp_sample[i]*rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max/P_gfp(pixels_sample[i])*z_gfp_max
                #yz_bins = yz_bins + yfp_sample[i]*rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max/P_yfp(pixels_sample[i])*z_yfp_max
                        
                xg_bins = xg_bins + growth_rate_sample[i]*gfp_sample[i]/P_gfp(pixels_sample[i])*z_gfp_max
                #yg_bins = yg_bins + growth_rate_sample[i]*yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max
                
                #xa_bins = xa_bins + areas_sample[i]*gfp_sample[i]/P_gfp(pixels_sample[i])*z_gfp_max
                #ya_bins = ya_bins + areas_sample[i]*yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max
    
                xx_bins = xx_bins + gfp_sample[i]*gfp_sample[i]/P_gfp(pixels_sample[i])*z_gfp_max/P_gfp(pixels_sample[i])*z_gfp_max
                #yy_bins = yy_bins + yfp_sample[i]*yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max/P_yfp(pixels_sample[i])*z_yfp_max
                zz_bins = zz_bins + rfp_sample[i]*rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max/P_rfp(pixels_sample[i])*z_rfp_max
            
                gg_bins = gg_bins + growth_rate_sample[i]*growth_rate_sample[i]
                #ll_bins = aa_bins + areas_sample[i]*areas_sample[i]
            
                #xy_bins = xy_bins + cfp_sample[i]*yfp_sample[i]/P_cfp(pixels_sample[i])*z_cfp_max/P_yfp(pixels_sample[i])*z_yfp_max
                
                number = number + 1
            
        if number > 0 :
            #print(number)
        
            
            gfp_average = gfp_average/number

            gfp_average_2 = gfp_average #- (cfp_average_b - 0*np.sqrt(varx_b))#*P_cfp((i+0.5)*bsize)/z_cfp_max
                
                
                
            rfp_average = rfp_average/number
                
            growth_rate_average = growth_rate_average/number
                
            xz_bins = xz_bins/number
            yz_bins = yz_bins/number
            
            xg_bins = xg_bins/number
            yg_bins = yg_bins/number
            xa_bins = xa_bins/number
            ya_bins = ya_bins/number
            
            xx_bins = xx_bins/number
            yy_bins = yy_bins/number
            zz_bins = zz_bins/number
            
            gg_bins = gg_bins/number
                
            xy_bins = xy_bins/number
            
            covxz = (xz_bins - gfp_average*rfp_average)
            
            covxg = (xg_bins - gfp_average*growth_rate_average)
            
            varx = (xx_bins - gfp_average**2)
            varz = (zz_bins - rfp_average**2)
            
            varg = (gg_bins - growth_rate_average**2)
            
            covxz_2 = covxz 
            
            covxg_2 = covxg
            #Final etas:
            etaxz = covxz_2/gfp_average_2/rfp_average
            
            etaxg = covxg_2/gfp_average_2/growth_rate_average
            
            
            rhoxz = covxz_2/np.sqrt(varx*varz)
            
            rhoxg = covxg_2/np.sqrt(varx*varg)
            
            cvz = np.sqrt(varz/rfp_average/rfp_average)
            cvg = np.sqrt(varg/growth_rate_average/growth_rate_average)

            etaxz_final.append(etaxz)
            
            etaxg_final.append(etaxg)
            
            rhoxz_final.append(rhoxz)
            
            rhoxg_final.append(rhoxg)
            
            xbar_final.append(gfp_average_2)
            
            gbar_final.append(growth_rate_average)
            zbar_final.append(rfp_average)

            cvz_final.append(cvz)
            cvg_final.append(cvg)
            print(sample)                          

etaxz_final = np.array(etaxz_final)
etayz_final = np.array(etayz_final)
rhoxz_final = np.array(rhoxz_final)
rhoyz_final = np.array(rhoyz_final)

etaxg_final = np.array(etaxg_final)
etayg_final = np.array(etayg_final)
rhoxg_final = np.array(rhoxg_final)
rhoyg_final = np.array(rhoyg_final)

etaxa_final = np.array(etaxa_final)
etaya_final = np.array(etaya_final)
rhoxa_final = np.array(rhoxa_final)
rhoya_final = np.array(rhoya_final)

ETAXZ = np.average(etaxz_final)
ETAXZ_ERR = np.std(etaxz_final)*2#/np.sqrt(number_of_samples-1)
ETAYZ = np.average(etayz_final)
ETAYZ_ERR = np.std(etayz_final)*2#/np.sqrt(number_of_samples-1)
RHOXZ = np.average(rhoxz_final)
RHOXZ_ERR = np.std(rhoxz_final)*2
RHOYZ = np.average(rhoyz_final)
RHOYZ_ERR = np.std(rhoyz_final)*2
XBAR = np.average(xbar_final)
XBAR_ERR = np.std(xbar_final)*2
YBAR = np.average(ybar_final)
YBAR_ERR = np.std(ybar_final)*2

ETAXG = np.average(etaxg_final)
ETAXG_ERR = np.std(etaxg_final)*2#/np.sqrt(number_of_samples-1)
ETAYG = np.average(etayg_final)
ETAYG_ERR = np.std(etayg_final)*2#/np.sqrt(number_of_samples-1)
RHOXG = np.average(rhoxg_final)
RHOXG_ERR = np.std(rhoxg_final)*2
RHOYG = np.average(rhoyg_final)
RHOYG_ERR = np.std(rhoyg_final)*2
GBAR = np.average(gbar_final)
GBAR_ERR = np.std(gbar_final)*2

ETAXA = np.average(etaxa_final)
ETAXA_ERR = np.std(etaxa_final)*2#/np.sqrt(number_of_samples-1)
ETAYA = np.average(etaya_final)
ETAYA_ERR = np.std(etaya_final)*2#/np.sqrt(number_of_samples-1)
RHOXA = np.average(rhoxa_final)
RHOXA_ERR = np.std(rhoxa_final)*2
RHOYA = np.average(rhoya_final)
RHOYA_ERR = np.std(rhoya_final)*2
ABAR = np.average(abar_final)
ABAR_ERR = np.std(abar_final)*2


ZBAR = np.average(zbar_final)
ZBAR_ERR = np.std(zbar_final)*2
GENERATION_TIME = np.average(time_to_divide)*5
cvz_final = np.array(cvz_final)
cvg_final = np.array(cvg_final)

CVZ = np.average(cvz_final)
CVZ_ERR = np.std(cvz_final)*2

CVG = np.average(cvg_final)
CVG_ERR = np.std(cvg_final)*2

"""

final_data = {'rfp_avg': ZBAR, 'rfp_avg_err': ZBAR_ERR,   \
              'growth_rate_avg': GBAR, 'growth_rate_avg_err': GBAR_ERR, \
              'generation_time': GENERATION_TIME, \
              'CVz': CVZ, 'CVz_err': CVZ_ERR, 'CVg': CVG, 'CVg_err': CVG_ERR}
    
    
with open('/Users/euan/Desktop/rpos-stuff/statistics/PA64_bootstrapping.pkl', 'wb') as f:
    pickle.dump(final_data, f)

"""
