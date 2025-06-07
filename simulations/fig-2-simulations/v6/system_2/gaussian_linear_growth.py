#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:22:36 2023

@author: mikdad
"""

import numpy as np
from scipy.stats import gamma


def gaussian_division(number_of_divisions):
                      
                          
    sigma = 0.2 #Sets the width of the gaussian distribution from which division times and factors are selected
    
    
    #number_of_divisions = 20000  #Todal number of division times and factors to save
    
    V0 = 1   #The initial volume. Cells grow on average from V0 to 2V0
    
    
    V = []    #The cell volume right after each division
    td = []  #The division times
    alpha = [] #The splitting factors at division times
    
    
    
    
    Vplot = [V0]   #These are just to plot the volume time traces
    #tplot = [0]
    
    
    #The first division: 
    #Getting division time:
    mu = 2*V0 - V0 #Set the center of the distribution to be when the cell would be 2*V0 
    w = 0
    while w < 1 :  #Making sure the selected division time is positive. 
        t = np.random.normal(mu, sigma, 1)[0]
        if t > 0:
            w = 1
    
    td.append(t)  
    
    #tplot.append(td[0])  #Saving twice because in plot we want to see volume 
    #tplot.append(td[0])   #  right before and right after division
    
    
    #Getting splitting factors:
    mu = V0/(V0 + t) #Set the center of the distribution to be the splitting factor that would 
                        # make the split cell to have size V0
                        
    
    w = 0
    while w < 1 :  #Making sure the selected splitting factor is positive and less than 1
        a = np.random.normal(mu, sigma, 1)[0]
        if a > 0 and a < 1:
            w = 1
    alpha.append(a)
    
    Vplot.append(V0 + t) #Saving to plot V right before splitting
    
    V.append(a*( V0 + t ))   #Saving right after split
    
    Vplot.append(V[0])  #Saving to plot V right after splitting
    
    
    
    #The rest of the divisions:
    for i in range(number_of_divisions - 1):
        
        
        #Getting division time:
        mu = 2*V0 - V[i] #Set the center of the distribution to be when the cell would be 2*V0 
        w = 0
        while w < 1 :  #Making sure the selected division time is positive. 
            t = np.random.normal(mu, sigma, 1)[0]
            if t > 0:
                w = 1
        
        td.append(td[i] + t)  
        
        #tplot.append(td[i+1])  #Saving twice because in plot we want to see volume 
        #tplot.append(td[i+1])   #  right before and right after division
        
        
        #Getting splitting factors:
        mu = V0/(V[i] + t) #Set the center of the distribution to be the splitting factor that would 
                            # make the split cell to have size V0
                            
        
        w = 0
        while w < 1 :  #Making sure the selected splitting factor is positive and less than 1
            a = np.random.normal(mu, sigma, 1)[0]
            if a > 0 and a < 1:
                w = 1
        alpha.append(a)
        
        Vplot.append(V[i] + t) #Saving to plot V right before splitting
        
        V.append(a*( V[i] + t ) )  #Saving right after split
        
        Vplot.append(V[i+1])  #Saving to plot V right after splitting
        
    return list(td), list(alpha), max(Vplot)

