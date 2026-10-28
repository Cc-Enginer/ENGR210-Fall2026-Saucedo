import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp

# System parameters

m = 0.20       # mass in kg

k = 20.0       # spring constant in N/m

x0 = 0.10      # initial displacement in m

v0 = 0.0       # initial velocity in m/s

# Example damping coefficients (illustrative)

c_air = 0.05       # N*s/m

c_water = 1.5      # N*s/m

# Time interval

t_start = 0.0

t_end = 30.0

number_of_points = 6001

t_eval = np.linspace(t_start, t_end, number_of_points)

# Stopping criteria

x_tolerance = 0.005   # displacement within 5 mm

v_tolerance = 0.01    # speed within 0.01 m/s

# Define the system of ODEs

def spring_mass(t, y, m, k, c):

    x, v = y

    dxdt = v

    dvdt = -(k / m) * x - (c / m) * v

    return [dxdt, dvdt]

# Solve the ODEs for one fluid

def simulate(c):

    solution = solve_ivp(

        spring_mass,

        (t_start, t_end),

        [x0, v0],

        args=(m, k, c),

        t_eval=t_eval,

        rtol=1e-8,

        atol=1e-10

    )

    if not solution.success:

        raise RuntimeError(solution.message)

    return solution.t, solution.y[0], solution.y[1]

# Estimate the settling time

def find_settling_time(t, x, v):

    within_limits = (

        (np.abs(x) <= x_tolerance)

        & (np.abs(v) <= v_tolerance)

    )

    # Find the first time both conditions remain satisfied

    # for the rest of the simulated time.

    stays_within_limits = np.logical_and.accumulate(

        within_limits[::-1]

    )[::-1]

    indices = np.where(stays_within_limits)[0]

    if len(indices) == 0:

        return None

    return t[indices[0]]

# Run simulations

t_air, x_air, v_air = simulate(c_air)

t_water, x_water, v_water = simulate(c_water)

settling_air = find_settling_time(t_air, x_air, v_air)

settling_water = find_settling_time(

    t_water, x_water, v_water

)

# Display results

print("MECHANICAL VIBRATIONS RESULTS")

print("-----------------------------")

if settling_air is None:

    print("Air: settling time not reached in simulation.")

else:

    print(f"Air settling time: {settling_air:.3f} s")

if settling_water is None:

    print("Water: settling time not reached in simulation.")

else:

    print(f"Water settling time: {settling_water:.3f} s")

if settling_air is not None and settling_water is not None:

    print(

        "Difference in settling time:",

        f"{settling_air - settling_water:.3f} s"

    )

# Plot displacement versus time

plt.figure(figsize=(10, 6))

plt.plot(t_air, x_air, label="Air")

plt.plot(t_water, x_water, label="Water")

plt.axhline(

    x_tolerance, linestyle="--",

    label="Displacement tolerance"

)

plt.axhline(-x_tolerance, linestyle="--")

plt.xlabel("Time (s)")

plt.ylabel("Displacement from equilibrium (m)")

plt.title("Damped Spring-Mass Vibrations in Air and Water")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()

