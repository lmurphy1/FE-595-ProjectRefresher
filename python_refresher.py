# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib as plt

import matplotlib.pylab as plt
x1 = np.linspace(0, 2*np.pi)
x2 = np.linspace(0,2*np.pi)
sin = plt.plot(x1, np.sin(x1), color = "red", label="sin")
cos = plt.plot(x2, np.cos(x2), color = "yellow", label="cos")
plt.xlabel('Angle (radians)')
plt.legend()
plt.show()