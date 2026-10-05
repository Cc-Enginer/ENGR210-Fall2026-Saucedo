import math
def f(t,y):
    return -1000 * y + 3000 -2000 * math.exp(-t)
def exact_solution(t):
    return (3
            - (997 /999) * math.exp(-1000 *t)
            - (2000/ 999) * math.exp(-t))

t_final = 0.01

time_steps = [0.0005, 0.00025, 0.000125, 0.0000625]

previous_error = None

for dt in time_steps:
    t = 0.0
    y = 0.0
    
    N = int(round(t_final / dt))
    
    sum_squared_errors = 0.0
    
    error = y - exact_solution(t)
    sum_squared_errors += error **2
    
    for i in range (N):
        
        k1 = f(t, y)
        
        y_predict = y + dt * k1
        
        k2 = f(t + dt, y_predict)
        
        y_new = y + (dt / 2) * (k1 +k2)
        
        t = t + dt
        y = y_new
        
        error = y-exact_solution(t)
        sum_squared_errors += error **2
        
    rmse = math.sqrt(sum_squared_errors / (N + 1))
    
    
    print("Time step:", dt)
    print("Approximate y:", y)
    print("Exact y:", exact_solution(t))
    print("RMS error:", rmse)
    
    if previous_error is not None:
        ratio = previous_error / rmse
        print("Previous error / current error:", ratio)
        
    print()
    previous_error = rmse
    
    
    
    
    
#Approximate y: 1.017871618698097
#Approximate y: 1.017871618698097
#Exact y: 1.017872941713404
#RMS error: 0.0004495394074311658
#Previous error / current error: 4.395526128986733

#Time step: 6.25e-05
#Approximate y: 1.0178726295038472
#Exact y: 1.017872941713404
#RMS error: 0.00010738938331236923
#Previous error / current error: 4.1860693633333055


    