import matplotlib.pyplot as plt

# Parameters

k_growth = 0.3     

k_predation = 0.01  

k_death = 0.2

k_hunt = 0.0003

# Initial conditions

prey0 = 700

predator0 = 22

# Time step = 1 month

# 1 month = 1/12 year

dt = 1/12

# Simulate for 10 years

years = 10

steps = int(years / dt)

# Lotka-Volterra equations

def derivatives(prey, predator):

    dprey = (

        k_growth * prey

        - k_predation * prey * predator

    )

    dpredator = (

        -k_death * predator

        + k_hunt * prey * predator

    )

    return dprey, dpredator

# -------------------------

# Euler Method

# -------------------------

time_euler = [0]

prey_euler = [prey0]

predator_euler = [predator0]

prey = prey0

predator = predator0

for i in range(steps):

    dprey, dpredator = derivatives(prey, predator)

    prey = prey + dt * dprey

    predator = predator + dt * dpredator

    time_euler.append((i + 1) * dt)

    prey_euler.append(prey)

    predator_euler.append(predator)

# -------------------------

# Heun's Method

# -------------------------

time_heun = [0]

prey_heun = [prey0]

predator_heun = [predator0]

prey = prey0

predator = predator0

for i in range(steps):

    # First slope

    dprey1, dpredator1 = derivatives(prey, predator)

    # Prediction

    prey_predict = prey + dt * dprey1

    predator_predict = predator + dt * dpredator1

    # Second slope

    dprey2, dpredator2 = derivatives(

        prey_predict,

        predator_predict

    )

    # Correction

    prey = prey + (dt / 2) * (dprey1 + dprey2)

    predator = predator + (dt / 2) * (

        dpredator1 + dpredator2

    )

    time_heun.append((i + 1) * dt)

    prey_heun.append(prey)

    predator_heun.append(predator)

# -------------------------

# Plot 1: Prey vs Time

# -------------------------

plt.figure()

plt.plot(time_euler, prey_euler, label="Euler")

plt.plot(time_heun, prey_heun, label="Heun")

plt.xlabel("Time (years)")

plt.ylabel("Prey Population")

plt.title("Prey Population vs Time")

plt.legend()

plt.grid()

plt.show()

# -------------------------

# Plot 2: Predators vs Time

# -------------------------

plt.figure()

plt.plot(time_euler, predator_euler, label="Euler")

plt.plot(time_heun, predator_heun, label="Heun")

plt.xlabel("Time (years)")

plt.ylabel("Predator Population")

plt.title("Predator Population vs Time")

plt.legend()

plt.grid()

plt.show()

# -------------------------

# Plot 3: Predator vs Prey

# -------------------------

plt.figure()

plt.plot(prey_euler, predator_euler, label="Euler")

plt.plot(prey_heun, predator_heun, label="Heun")

plt.xlabel("Prey Population")

plt.ylabel("Predator Population")

plt.title("Predator vs Prey")

plt.legend()

plt.grid()

plt.show()

