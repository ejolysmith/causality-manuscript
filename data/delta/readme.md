Directories contain purged single cell trajectories from mother machine experiments for each respective strain (see SI for circuit, strain, and plasmid details). 

In each strain directory, there are pickle files for cell yfp, cfp, and rfp fluorescence measurements (avg. intensity across segmented area), 
as well as cell area, length, frame, and horizontal position (xpixels). These files are divided according to non-overlapping fields of view that 
contain a different set of cells. 

For instance, for cells in field of view defined as pos12, there is the following:
cfp_purged_pos12-purge2.pkl (a series of lists of cfp measurements, where each list is a cell, and each element is a single time point snapshot).
yfp_purged_pos12-purge2.pkl (same but yfp).
rfp_purged_pos12-purge2.pkl (same buy rfp).
areas_purged_pos12-purge2.pkl (same but single cell segmented areas).
lengths_purged_pos12-purge2.pkl (same but single cell length).
frames_purged_pos12-purge2.pkl (a series of lists where each list is a cell, and each element is the time point indice at which measurment was taken).
frames_purged_xpixels12-purge2.pkl (a single list where each element is the x position of a cell in FOV in pixels).

In addition, analogous files are added with subscript "_b" in filename which correpsond to cells that have lost the plasmid. These are used 
for background signal correction. 

In each strain directory, a python script called "analyze_bootstrapping_delta.." takes these traces, corrects for uneven illumination, 
background signal, and drift, and then computes normalized covariances estimating errorbars using bootsrapping (see Fig S16 A in SI). 
The "analyze_split_delta.." is similar but uses the approach described in Fig S17 B in SI to estimate uncertainty. 

Final normalized covariances are saved in final_statistics directory. 
