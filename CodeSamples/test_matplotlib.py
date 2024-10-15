#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:30:56 2024

@author: uwejaekel
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)
plt.figure() # Neue Abbildung
plt.plot(x, np.sin(x));
