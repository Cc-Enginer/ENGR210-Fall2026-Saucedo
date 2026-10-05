#HW05 problem 2

import math
def f(t, y):
    return -y

def exact_solution(t):
    return math.exp(-t)

t_final = 5.0

time_steps = [1.0, 0.5, 0.25, 0.125]


previous_error = None
for dt in time_steps:
    
    t = 0.0
    y= 1.0
    
    N = int(round(t_final / dt))
    sum_squared_errors = 0.0

    for i in range(N):
        error = y-exact_solution(t)
        sum_squared_errors += error **2
    
        k1= f(t,y)
    
        k2 = f(t + dt /2,
           y + dt * k1 /2)
    
        k3 = f(t + dt /2,
           y + dt * k2 /2)
    
        k4 = f(t + dt,
           y + dt * k3)
    
    #Update Solution
        y = y + (dt /6) * (
        k1 + 2 * k2 + 2 * k3 + k4)
    
        t = t + dt
    
    rmse = math.sqrt(dt * sum_squared_errors)

    print("Time step:", dt)
    print("Approximate y:", y)
    print("Exact y:", exact_solution(t))
    print("RMS error:", rmse)

    if previous_error is not None:
        order = math.log(
            previous_error/ rmse, 2
        )
        print("Estimated order:", order)
    
    print()
    previous_error = rmse 
    
    
    
    
    
    