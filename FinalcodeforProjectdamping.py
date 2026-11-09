import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --------------------------------
# 1. SYSTEM PARAMETERS
# --------------------------------

m = 1.0          # Mass (kg)
k = 20.0         # Spring stiffness (N/m)

c_air = 0.08     # Damping coefficient in air
c_water = 2.0    # Damping coefficient in water

x0 = 0.10        # Initial displacement (m)
v0 = 0.0         # Initial velocity (m/s)

t_start = 0
t_end = 120
number_of_points = 2000

# --------------------------------
# 2. INITIAL ENERGY
# --------------------------------

E0 = 0.5 * m * v0**2 + 0.5 * k * x0**2

# --------------------------------
# 3. DIFFERENTIAL EQUATIONS
# --------------------------------

def spring_mass(t, y, c):

    x, v = y

    dxdt = v

    dvdt = (-k*x - c*v) / m

    return [dxdt, dvdt]

# --------------------------------
# 4. SIMULATION FUNCTION
# --------------------------------

def simulate(c):

    time = np.linspace(
        t_start,
        t_end,
        number_of_points
    )

    solution = solve_ivp(
        spring_mass,
        [t_start, t_end],
        [x0, v0],
        args=(c,),
        t_eval=time,
        method='RK45',
        rtol=1e-8,
        atol=1e-10
    )

    x = solution.y[0]
    v = solution.y[1]

    # Calculate kinetic energy
    kinetic_energy = 0.5 * m * v**2

    # Calculate spring potential energy
    potential_energy = 0.5 * k * x**2

    # Calculate total mechanical energy
    total_energy = kinetic_energy + potential_energy

    # Calculate energy lost
    energy_lost = E0 - total_energy

    return time, x, v, total_energy, energy_lost

# --------------------------------
# 5. RUN BOTH SIMULATIONS
# --------------------------------

air = simulate(c_air)
water = simulate(c_water)

# --------------------------------
# 6. FIND TIME TO REACH 1% ENERGY
# --------------------------------

def settling_time(time, energy):

    target_energy = 0.01 * E0

    indices = np.where(energy <= target_energy)[0]

    if len(indices) == 0:
        return None

    i = indices[0]

    if i == 0:
        return time[0]

    # Interpolate between data points
    return np.interp(
        target_energy,
        energy[i-1:i+1][::-1],
        time[i-1:i+1][::-1]
    )

air_time = settling_time(air[0], air[3])
water_time = settling_time(water[0], water[3])

# --------------------------------
# 7. DISPLAY RESULTS
# --------------------------------

print("MECHANICAL VIBRATIONS RESULTS")
print("--------------------------------")

print("Initial Energy:", round(E0, 5), "J")

print("Air Damping Coefficient:", c_air)
print("Water Damping Coefficient:", c_water)

print("--------------------------------")

if air_time is not None:
    print("Time to reach 1% energy in air:",
          round(air_time, 3), "seconds")
else:
    print("Air did not reach 1% energy.")

if water_time is not None:
    print("Time to reach 1% energy in water:",
          round(water_time, 3), "seconds")
else:
    print("Water did not reach 1% energy.")

if air_time is not None and water_time is not None:
    print("--------------------------------")
    print("Air / Water settling time ratio:",
          round(air_time / water_time, 2))

# --------------------------------
# 8. PLOT DISPLACEMENT
# --------------------------------

plt.figure(figsize=(10, 5))

plt.plot(air[0], air[1], label="Air")
plt.plot(water[0], water[1], label="Water")

plt.xlabel("Time (seconds)")
plt.ylabel("Displacement (meters)")
plt.title("Mass-Spring Displacement in Air vs. Water")

plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# --------------------------------
# 9. PLOT TOTAL ENERGY
# --------------------------------

plt.figure(figsize=(10, 5))

plt.plot(air[0], air[3] / E0, label="Air")
plt.plot(water[0], water[3] / E0, label="Water")

plt.axhline(
    y=0.01,
    linestyle="--",
    label="1% Initial Energy"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Fraction of Initial Energy Remaining")
plt.title("Energy Decay: Air vs. Water")

plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# --------------------------------
# 10. PLOT ENERGY LOST
# --------------------------------

plt.figure(figsize=(10, 5))

plt.plot(air[0], air[4], label="Air")
plt.plot(water[0], water[4], label="Water")

plt.xlabel("Time (seconds)")
plt.ylabel("Energy Lost (Joules)")
plt.title("Energy Dissipation in Air vs. Water")

plt.legend()
plt.grid()
plt.tight_layout()
plt.show()