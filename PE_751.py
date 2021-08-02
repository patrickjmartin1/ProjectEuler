"""
Concatenation Coincidence
"""
from math import floor
from mpmath import mp
mp.dps = 50
import numpy as np


def get_tau(theta):
    tau = "2."
    b = theta
    while len(tau) <= 50:
        b = floor(b) * (b - floor(b) + 1)
        tau = tau + str(floor(b))
    return tau


if __name__ == "__main__":
    # Seed values
    x = .1
    theta = mp.mpf(2 + x)
    tau = get_tau(theta)

    while str(theta)[:26] != tau[:26]:
        x = mp.mpf(tau) - floor(float(tau))
        theta = mp.mpf(2 + x)
        tau = get_tau(theta)
        print("Theta: {}, Tau: {}".format(str(theta), tau))
        print("diff: {}".format(theta - float(tau)))

    print(tau[:26])

    """
    This produces the correct answer: 2.223561019313554106173177
    """