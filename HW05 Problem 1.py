#HW05 problem 1

import numpy as np
import matplotlib as plt

import math

t_final = 5.0

time_steps = [1.0,0.5, 0.25, 0.125]

for dt in time_steps:
    t= 0.0
    y = 1.0
    
    N = int(round(t_final / dt))
    
    sum_squared_errors = 0.0
    
    for i in range(N):
        
        y_exact = math.exp(-t)
        
        error = y-y_exact
        sum_squared_errors += error ** 2
        
        y_new = y - y * dt
        
        y = y_newy = t + dt
        
    rmse = math.sqrt(dt * sum_squared_errors)
    
    
    print("time steo:", dt)
    print("Approximate y at t = ", t, ":", y)
    print("RMS error:", rmse)
    print()
    
#     
# 
# t =[]
# y= []
# 
# 
# def fyt_func(t,y):
#     
