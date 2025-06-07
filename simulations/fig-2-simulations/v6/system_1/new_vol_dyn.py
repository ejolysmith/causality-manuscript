#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:22:18 2023

@author: mikdad
"""

import numpy as np

def flatten_3d(result): #To seperate results after using pool to parallelize
        
    eta_xz = []
    eta_yz = []
    eta_xz_error = []
    eta_yz_error = []
    pearson_xz = []
    pearson_yz = []
    pearson_xz_error = []
    pearson_yz_error = []
    eta_xz_numbers = []
    eta_yz_numbers = []
    eta_xz_error_numbers = []
    eta_yz_error_numbers = []
    pearson_xz_numbers = []
    pearson_yz_numbers = []
    pearson_xz_error_numbers = []
    pearson_yz_error_numbers = []
    lamda = []
    lamda_z = []
    lamda_w = []
    beta_x = []
    beta_y = []
    beta_z = []
    beta_w = []
    k = []
    number_of_simulations = []
    for i in range(0, len(result)):
        tuple_result= result[i]
        eta_xz.append(tuple_result[0])
        eta_yz.append(tuple_result[1])
        eta_xz_error.append(tuple_result[2])
        eta_yz_error.append(tuple_result[3])
        pearson_xz.append(tuple_result[4])
        pearson_yz.append(tuple_result[5])
        pearson_xz_error.append(tuple_result[6])
        pearson_yz_error.append(tuple_result[7])
        
        eta_xz_numbers.append(tuple_result[8])
        eta_yz_numbers.append(tuple_result[9])
        eta_xz_error_numbers.append(tuple_result[10])
        eta_yz_error_numbers.append(tuple_result[11])
        pearson_xz_numbers.append(tuple_result[12])
        pearson_yz_numbers.append(tuple_result[13])
        pearson_xz_error_numbers.append(tuple_result[14])
        pearson_yz_error_numbers.append(tuple_result[15])
        
        lamda.append(tuple_result[16])
        lamda_z.append(tuple_result[17])
        lamda_w.append(tuple_result[18])
        beta_x.append(tuple_result[19])
        beta_y.append(tuple_result[20])
        beta_z.append(tuple_result[21])
        beta_w.append(tuple_result[22])
        k.append(tuple_result[23])
        number_of_simulations.append(tuple_result[24])
        
    eta_xz = np.array(eta_xz)
    eta_xz = eta_xz.flatten()
    
    eta_yz = np.array(eta_yz)
    eta_yz = eta_yz.flatten()
    
    eta_xz_error = np.array(eta_xz_error)
    eta_xz_error = eta_xz_error.flatten()
    
    eta_yz_error = np.array(eta_yz_error)
    eta_yz_error = eta_yz_error.flatten()
    
    pearson_xz = np.array(pearson_xz)
    pearson_xz = pearson_xz.flatten()
    
    pearson_yz = np.array(pearson_yz)
    pearson_yz = pearson_yz.flatten()
    
    pearson_xz_error = np.array(pearson_xz_error)
    pearson_xz_error = pearson_xz_error.flatten()
    
    pearson_yz_error = np.array(pearson_yz_error)
    pearson_yz_error = pearson_yz_error.flatten()
    
    eta_xz_numbers = np.array(eta_xz_numbers)
    eta_xz_numbers = eta_xz_numbers.flatten()
    
    eta_yz_numbers = np.array(eta_yz_numbers)
    eta_yz_numbers = eta_yz_numbers.flatten()
    
    eta_xz_error_numbers = np.array(eta_xz_error_numbers)
    eta_xz_error_numbers = eta_xz_error_numbers.flatten()
    
    eta_yz_error_numbers = np.array(eta_yz_error_numbers)
    eta_yz_error_numbers = eta_yz_error_numbers.flatten()
    
    pearson_xz_numbers = np.array(pearson_xz_numbers)
    pearson_xz_numbers = pearson_xz_numbers.flatten()
    
    pearson_yz_numbers = np.array(pearson_yz_numbers)
    pearson_yz_numbers = pearson_yz_numbers.flatten()
    
    pearson_xz_error_numbers = np.array(pearson_xz_error_numbers)
    pearson_xz_error_numbers = pearson_xz_error_numbers.flatten()
    
    pearson_yz_error_numbers = np.array(pearson_yz_error_numbers)
    pearson_yz_error_numbers = pearson_yz_error_numbers.flatten()
    
    
    
    lamda = np.array(lamda)
    lamda = lamda.flatten()
    
    lamda_z = np.array(lamda_z)
    lamda_z = lamda_z.flatten()
    
    lamda_w = np.array(lamda_w)
    lamda_w = lamda_w.flatten()
    
    beta_x = np.array(beta_x)
    beta_x = beta_x.flatten()
    
    beta_y = np.array(beta_y)
    beta_y = beta_y.flatten()
    
    beta_z = np.array(beta_z)
    beta_z = beta_z.flatten()
    
    beta_w = np.array(beta_w)
    beta_w = beta_w.flatten()
    
    k = np.array(k)
    k.flatten()
    
    number_of_simulations = np.array(number_of_simulations)
    number_of_simulations.flatten()
    
    
    return eta_xz, eta_yz, eta_xz_error, eta_yz_error, pearson_xz, pearson_yz, pearson_xz_error, pearson_yz_error,eta_xz_numbers, eta_yz_numbers, eta_xz_error_numbers, eta_yz_error_numbers, pearson_xz_numbers, pearson_yz_numbers, pearson_xz_error_numbers, pearson_yz_error_numbers, lamda, lamda_z, lamda_w, beta_x, beta_y, beta_z, beta_w, k, number_of_simulations




a = np.log(2) #Parameter for exponentially growing volume i.e. V = exp(a * t)
b = 1 #Parameter for linearly growing volume i.e. V = V0 + b * t

def running_abundance_avg(x, prev_x_avg, current_waittime, current_time):
    ''' Computes a running average of x from 0 upto current_time. Inputs previous x average
    i.e. the average of x from 0 upto current_time - current_waittime , the waittime of x in its current state,
    and the current value of x i.e. the value of x from current_time - current_waittime to current_time
    '''
    average = prev_x_avg * (current_time - current_waittime)/(current_time) + x * current_waittime / current_time
    
    return average

def exp_V(V0, t):
    '''Returns value of volume for exponentially growing cell at time t
    '''
    V = V0 * np.exp(a * t)

    return V

def lin_V(V0, t):
    '''Returns value of volume for linearly growing cell at time t
    '''
    V = V0 + b * t
    
    return V

def lin_V_integral(V0, t):
    '''Returns value of antiderivative for volume of linearly growing cell evaluated at time t
    '''
    
    V_int = V0 * t + b * (t ** 2 ) / 2
    
    return V_int


def lin_one_over_V_integral(V0,  t):
    '''Returns value of antiderivative for 1/volume of linearly growing cell evaluated at time t
    '''
    V_int = (np.log(b * t + V0)) / b
    return V_int

def lin_one_over_V_sq_integral(V0, t):
    '''Returns value of antiderivative for 1/volume**2 of linearly growing cell evaluated at time t
    '''
    V_int = -1 / (b * (b * t + V0))
    
    return V_int

def exp_V_integral(V0, t):
    '''Returns value of antiderivative for volume of exponentially growing cell evaluated at time t
    '''
    V_int = V0 * np.exp(a  * t) / a
    
    return V_int

def exp_one_over_V_integral(V0 , t):
    '''Returns value of antiderivative for 1/volume of exponentially growing cell evaluated at time t
    '''
    
    V_int = -(np.exp(-a * t))/(a * V0)
    
    return V_int

def exp_one_over_V_sq_integral(V0,  t):
    '''Returns value of antiderivative for 1/volume**2 of exponentially growing cell evaluated at time t
    '''
    
    V_int = -(np.exp(-2 * a * t)) / (2 * a * (V0 ** 2))
    
    return V_int

def lin_vol_average(current_vol, prev_vol_average, current_waittime, current_time, interval_time):
    average = prev_vol_average * (current_time - current_waittime) / current_time + (current_waittime / current_time) * (lin_V_integral(current_vol, interval_time) - lin_V_integral(current_vol, interval_time - current_waittime))
    return average

def temp_lin_one_over_vol_average(current_vol, current_waittime, interval_time):
    average = lin_one_over_V_integral(current_vol, interval_time) - lin_one_over_V_integral(current_vol, interval_time - current_waittime)
    return average

def temp_lin_one_over_vol_sq_average(current_vol, current_waittime, interval_time):
    average = lin_one_over_V_sq_integral(current_vol, interval_time) - lin_one_over_V_sq_integral(current_vol, interval_time - current_waittime)
    return average
    
def exp_vol_average(current_vol, prev_vol_average, current_waittime, current_time, interval_time):
    average = prev_vol_average * (current_time - current_waittime) / current_time + (current_waittime / current_time) * (exp_V_integral(current_vol, interval_time) - exp_V_integral(current_vol, interval_time - current_waittime))
    return average

def temp_exp_one_over_vol_average(current_vol, current_waittime, interval_time):
    average = exp_one_over_V_integral(current_vol, interval_time) - exp_one_over_V_integral(current_vol, interval_time - current_waittime)
    return average

def temp_exp_one_over_vol_sq_average(current_vol, current_waittime, interval_time):
    average = exp_one_over_V_sq_integral(current_vol, interval_time) - exp_one_over_V_sq_integral(current_vol, interval_time - current_waittime)
    return average