"""
Laura Murphy
FE 595 Python Refresher
"""

import numpy as np
import matplotlib.pyplot as plt


def plot():
    x = np.linspace(0, 2 * np.pi, num=500)
    plt.plot(x, np.sin(x), color="red", label="sin")
    plt.plot(x, np.cos(x), color="blue", label="cos")
    plt.xlabel("Angle (radians)")
    plt.legend()
    plt.show()

def add_experiment():
    print("hi!")


if __name__ == "__main__":
    plot()
    add_experiment()
