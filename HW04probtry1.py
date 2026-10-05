#HW04 prob 2

import numpy as np

def trapezoidal_rule(x, y):

    h = np.diff(x)

    integral = np.sum(

        h * (y[:-1] + y[1:]) / 2

    )

    return integral

if __name__ == "__main__":

    # Load the stress-strain data

    data = np.loadtxt("C:\Users\Cc Saucedo\OneDrive - Saint Francis University\Documents\Simple_Quad\Engr210",

                      delimiter=",",

                      skiprows=1)

    strain = data[:, 1]

    stress = data[:, 0]

    # Only use data up to the rupture strain

    rupture_strain = 0.25

    mask = strain <= rupture_strain

    strain = strain[mask]

    stress = stress[mask]

    # Calculate the area under the stress-strain curve

    toughness = trapezoidal_rule(strain, stress)

    print("Modulus of toughness =", toughness)

