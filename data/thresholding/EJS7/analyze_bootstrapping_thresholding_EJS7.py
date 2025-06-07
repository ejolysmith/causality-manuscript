import numpy as np
import pickle
import random

#Loading data from the purged time traces from matlab pipeline:
    
#The cells with plasmid:
pixels = np.loadtxt('cenx_EJS7.txt', delimiter = ',')
cfp = np.loadtxt('cfp_EJS7.txt', delimiter = ',')
yfp = np.loadtxt('yfp_EJS7.txt', delimiter = ',')
rfp = np.loadtxt('rfp_EJS7.txt', delimiter = ',')
growth_rate = np.loadtxt('growthrate_EJS7.txt', delimiter = ',')
areas = np.loadtxt('area_EJS7.txt', delimiter = ',')
frames = np.loadtxt('frame_EJS7.txt', delimiter = ',')
cell_number = np.loadtxt('cellNo_EJS7.txt', delimiter = ',')
fov = np.loadtxt('FOV_EJS7.txt', delimiter = ',')



number_of_positions = len(np.unique(fov))
fov_unique = np.unique(fov)
cfp_cells = []
rfp_cells = []
yfp_cells = []
pixels_cells = []
frames_cells = []
areas_cells = []
growth_rate_cells = []


#Splitting data into single cell arrays
for i in range(number_of_positions):
    position = fov_unique[i]
    indexes = np.where(fov == position)
    max_cell_number = int(np.max(cell_number[indexes]))
    for j in range(max_cell_number):
        cell_number_position = j + 1
        cell_indexes = np.where(cell_number[indexes] == cell_number_position)
        cfp_cells.append(cfp[indexes][cell_indexes])
        rfp_cells.append(rfp[indexes][cell_indexes])
        yfp_cells.append(yfp[indexes][cell_indexes])
        pixels_cells.append(pixels[indexes][cell_indexes])
        frames_cells.append(frames[indexes][cell_indexes])
        areas_cells.append(areas[indexes][cell_indexes])
        growth_rate_cells.append(growth_rate[indexes][cell_indexes])     
        
        


number_of_cells = len(cfp_cells)

#Number of samples for bootstrapping
number_of_samples = 100



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



max_frame = 150

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
        random_cell = random.randint(0, number_of_cells-1)
        for k in range(len(frames_cells[random_cell])):
            cfp_sample.append(cfp_cells[random_cell][k])
            yfp_sample.append(yfp_cells[random_cell][k])
            rfp_sample.append(rfp_cells[random_cell][k])
            pixels_sample.append(pixels_cells[random_cell][k])
            frames_sample.append(frames_cells[random_cell][k])
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

        
    Z = np.polyfit(np.array(range(50, len(yfp_time_bins))), yfp_time_bins[50:], 2)
    P = np.poly1d(Z)

    for i in range(len(yfp_sample)):
        if frames_sample[i] < number_of_frames :
            yfp_sample[i] = yfp_sample[i]/P(int(frames_sample[i]))*P(50)
            
        
    Z = np.polyfit(np.array(range(50, len(cfp_time_bins))), cfp_time_bins[50:], 2)
    P = np.poly1d(Z)

    for i in range(len(cfp_sample)):
            if frames_sample[i] < number_of_frames :
                cfp_sample[i] = cfp_sample[i]/P(int(frames_sample[i]))*P(50)


    
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
            
            yz_bins = yz_bins + cfp_sample[i]*rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max/P_cfp(pixels_sample[i])*z_cfp_max
            xz_bins = xz_bins + yfp_sample[i]*rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max/P_yfp(pixels_sample[i])*z_yfp_max
                    
            yg_bins = yg_bins + growth_rate_sample[i]*cfp_sample[i]/P_cfp(pixels_sample[i])*z_cfp_max
            xg_bins = xg_bins + growth_rate_sample[i]*yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max

            yy_bins = yy_bins + cfp_sample[i]*cfp_sample[i]/P_cfp(pixels_sample[i])*z_cfp_max/P_cfp(pixels_sample[i])*z_cfp_max
            xx_bins = xx_bins + yfp_sample[i]*yfp_sample[i]/P_yfp(pixels_sample[i])*z_yfp_max/P_yfp(pixels_sample[i])*z_yfp_max
            zz_bins = zz_bins + rfp_sample[i]*rfp_sample[i]/P_rfp(pixels_sample[i])*z_rfp_max/P_rfp(pixels_sample[i])*z_rfp_max
        
            gg_bins = gg_bins + growth_rate_sample[i]*growth_rate_sample[i]
        
            xy_bins = xy_bins + cfp_sample[i]*yfp_sample[i]/P_cfp(pixels_sample[i])*z_cfp_max/P_yfp(pixels_sample[i])*z_yfp_max
            
            number = number + 1
        
    if number > 0 :
        #print(number)
    
        
        cfp_average = cfp_average/number
        #Correcting the autofluorescnece/background:
        cfp_average_2 = cfp_average 
            
            
        yfp_average = yfp_average/number
        #Correcting the autofluorescnece/background:
        yfp_average_2 = yfp_average
            
        rfp_average = rfp_average/number
            
        growth_rate_average = growth_rate_average/number
        lengths_average = lengths_average/number
            
        xz_bins = xz_bins/number
        yz_bins = yz_bins/number
        
        xg_bins = xg_bins/number
        yg_bins = yg_bins/number
        
        xx_bins = xx_bins/number
        yy_bins = yy_bins/number
        zz_bins = zz_bins/number
        
        gg_bins = gg_bins/number
            
        xy_bins = xy_bins/number
        
        covyz = (yz_bins - cfp_average*rfp_average)
        covxz = (xz_bins - yfp_average*rfp_average)
        
        covyg = (yg_bins - cfp_average*growth_rate_average)
        covxg = (xg_bins - yfp_average*growth_rate_average)
        
        vary = (yy_bins - cfp_average**2)
        varx = (xx_bins - yfp_average**2)
        varz = (zz_bins - rfp_average**2)
        
        varg = (gg_bins - growth_rate_average**2)
        
        vary_2 = vary 
        varx_2 = varx 
        
        
        #Correcting for background/autofluorescence covariance:
        covxz_2 = covxz 
        covyz_2 = covyz 
        
        
        covxg_2 = covxg 
        covyg_2 = covyg 
        
        #Final etas:
        etayz = covyz_2/cfp_average_2/rfp_average
        etaxz = covxz_2/yfp_average_2/rfp_average
        
        etayg = covyg_2/cfp_average_2/growth_rate_average
        etaxg = covxg_2/yfp_average_2/growth_rate_average
        
        
        rhoxz = covxz_2/np.sqrt(varx_2*varz)
        rhoyz = covyz_2/np.sqrt(vary_2*varz)
        
        rhoxg = covxg_2/np.sqrt(varx_2*varg)
        rhoyg = covyg_2/np.sqrt(vary_2*varg)
        
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


ETAXZ = np.average(etaxz_final)
ETAXZ_ERR = np.std(etaxz_final)*2
ETAYZ = np.average(etayz_final)
ETAYZ_ERR = np.std(etayz_final)*2
RHOXZ = np.average(rhoxz_final)
RHOXZ_ERR = np.std(rhoxz_final)*2
RHOYZ = np.average(rhoyz_final)
RHOYZ_ERR = np.std(rhoyz_final)*2
XBAR = np.average(xbar_final)
XBAR_ERR = np.std(xbar_final)*2
YBAR = np.average(ybar_final)
YBAR_ERR = np.std(ybar_final)*2

ZBAR = np.average(zbar_final)
ZBAR_ERR = np.std(zbar_final)*2


ETAXG = np.average(etaxg_final)
ETAXG_ERR = np.std(etaxg_final)*2
ETAYG = np.average(etayg_final)
ETAYG_ERR = np.std(etayg_final)*2
RHOXG = np.average(rhoxg_final)
RHOXG_ERR = np.std(rhoxg_final)*2
RHOYG = np.average(rhoyg_final)
RHOYG_ERR = np.std(rhoyg_final)*2
GBAR = np.average(gbar_final)
GBAR_ERR = np.std(gbar_final)*2




final_data = {'etaxz': ETAXZ, 'etaxz_err': ETAXZ_ERR, 'etayz': ETAYZ, 'etayz_err': ETAYZ_ERR, \
              'etaxg': ETAXG, 'etaxg_err': ETAXG_ERR, 'etayg': ETAYG, 'etayg_err': ETAYG_ERR, \
              'xavg' : XBAR,  'xavg_err' : XBAR_ERR,  'yavg' : YBAR,  'yavg_err' : YBAR_ERR,  \
              'growth_rate_avg': GBAR, 'growth_rate_avg_err': GBAR_ERR}
    
    
with open('../thresholding_final_statistics/EJS7_thresholding.pkl', 'wb') as f:
    pickle.dump(final_data, f)


