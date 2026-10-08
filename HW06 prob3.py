import math

import matplotlib.pyplot as plt

# Constants

m = 2.0

k = 20.0

x0 = 0.5

v0 = 0.0

dt = 0.1

total_time = 200.0

steps = int(total_time / dt)

# Acceleration

def acceleration(x):

    return -(k / m) * x

# Exact solution

def exact_solution(t):

    omega = math.sqrt(k / m)

    return x0 * math.cos(omega * t)

# ==================================================

# EULER METHOD

# ==================================================

time_euler = []

x_euler = []

x = x0

v = v0

for i in range(steps + 1):

    t = i * dt

    time_euler.append(t)

    x_euler.append(x)

    a = acceleration(x)

    x = x + dt * v

    v = v + dt * a

# ==================================================

# RUNGE-KUTTA 4 METHOD

# ==================================================

time_rk = []

x_rk = []

x = x0

v = v0

def rk4_step(x, v, dt):

    # k1

    k1_x = v

    k1_v = acceleration(x)

    # k2

    k2_x = v + 0.5 * dt * k1_v

    k2_v = acceleration(x + 0.5 * dt * k1_x)

    # k3

    k3_x = v + 0.5 * dt * k2_v

    k3_v = acceleration(x + 0.5 * dt * k2_x)

    # k4

    k4_x = v + dt * k3_v

    k4_v = acceleration(x + dt * k3_x)

    new_x = x + (dt / 6) * (

        k1_x + 2*k2_x + 2*k3_x + k4_x

    )

    new_v = v + (dt / 6) * (

        k1_v + 2*k2_v + 2*k3_v + k4_v

    )

    return new_x, new_v

for i in range(steps + 1):

    t = i * dt

    time_rk.append(t)

    x_rk.append(x)

    x, v = rk4_step(x, v, dt)

# ==================================================

# LEAPFROG METHOD

# ==================================================

time_lf = []

x_lf = []

x = x0

v = v0

# Initial half-step velocity

v_half = v + 0.5 * dt * acceleration(x)

for i in range(steps + 1):

    t = i * dt

    time_lf.append(t)

    x_lf.append(x)

    # Update position

    x = x + dt * v_half

    # Update velocity at half step

    v_half = v_half + dt * acceleration(x)

# ==================================================

# CALCULATE ERRORS

# ==================================================

error_euler = []

error_rk = []

error_lf = []

for i in range(len(time_euler)):

    exact = exact_solution(time_euler[i])

    error_euler.append(

        abs(x_euler[i] - exact)

    )

    error_rk.append(

        abs(x_rk[i] - exact)

    )

for i in range(len(time_lf)):

    exact = exact_solution(time_lf[i])

    error_lf.append(

        abs(x_lf[i] - exact)

    )

# ==================================================

# PLOT ERROR

# ==================================================

plt.figure()

plt.plot(time_euler, error_euler, label="Euler")

plt.plot(time_rk, error_rk, label="RK4")

plt.plot(time_lf, error_lf, label="Leapfrog")

plt.xlabel("Time (seconds)")

plt.ylabel("Absolute Error (m)")

plt.title("Mass/Spring Numerical Error")

plt.legend()

plt.grid()

plt.show()

# ==================================================

# PLOT MOTION

# ==================================================

plt.figure()

plt.plot(time_euler, x_euler, label="Euler")

plt.plot(time_rk, x_rk, label="RK4")

plt.plot(time_lf, x_lf, label="Leapfrog")

plt.xlabel("Time (seconds)")

plt.ylabel("Displacement (m)")

plt.title("Mass/Spring Motion")

plt.legend()

plt.grid()

plt.show()

# ==================================================

# PRINT FINAL ERRORS

# ==================================================

print("Final Euler error:", error_euler[-1])

print("Final RK4 error:", error_rk[-1])

print("Final Leapfrog error:", error_lf[-1])