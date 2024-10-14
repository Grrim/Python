# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 13:56:06 2021

@author: Grim
"""

import math
import matplotlib.pyplot as plt
from math import e
import numpy as np

def decreaseInRadioSignalStrength(Gt, Gr, f, d, c, lenght, step):
    values = []
    a = []    
    g = []
    radioWaveLength = c/f
    while d < lenght:
        x = Gt * Gr * ((radioWaveLength / ((4 * math.pi) * d)) **2)
        s = 10 * math.log10(x)
        values.append(s)
        a.append(d)
        g.append(c)
        print(x)
        d = d + step        
    plt.plot(a, values)
    plt.xlabel("[m]")
    plt.ylabel("[dB]")
    return values;

#decreaseInRadioSignalStrength(1.6, 1.6, 900000000, 1, 299792458, 100, 1)
#decreaseInRadioSignalStrength(1.6, 1.6, 900000000, 1, 299792458, 10000, 10)

def SignalDelay(Gt, Gr, f, d, c, lenght, step):
    values = []
    a = []    
    g = []
    radioWaveLength = c/f
    while d < lenght:
        x = Gt * Gr * ((radioWaveLength / ((4 * math.pi) * d)) **2)
        s = 10 * math.log10(x)
        p = ((8)**2 + (d)**2)
        eq = np.sqrt(p) * c
        values.append(s)
        a.append(d)
        g.append(eq)
        print(x)
        d = d + step        
    plt.plot(a, g)
    plt.xlabel("[m]")
    plt.ylabel("opóźnienie")
    return values;

#SignalDelay(1.6, 1.6, 900000000, 1, 299792458, 100, 1)
SignalDelay(1.6, 1.6, 900000000, 1, 299792458, 10000, 10)

def decreaseInRadioSignalStrengthInTwoWays(Gt, Gr, f, d, c, lenght, step, h1, h2):
    values = []
    a = []      
    radioWaveLength = c/f
    print(radioWaveLength)
    while d < lenght:
        d1 = math.sqrt(((h1-h2)**2) + (d**2))
        d2 = math.sqrt(((h1+h2)**2) + (d**2))
        omega1 = (-2 * math.pi * f * (d1/c))
        omega2 = (-2 * math.pi * f * (d2/c))
        Pr = abs(((1/d1)*(e**(1j*omega1))) - ((1/d2)*(e**(1j*omega2))))
        x = Gt * Gr * ((radioWaveLength / (4 * math.pi))**2) * Pr
        s = 10 * math.log10(x)
        values.append(s)
        a.append(d)
        d = d + step
    plt.plot(a, values)
    plt.xlabel("[m]")
    plt.ylabel("[dB]")
    
#decreaseInRadioSignalStrengthInTwoWays(1.6, 1.6, 900000000, 1, 299792458, 100, 0.25, 30, 3)
#decreaseInRadioSignalStrengthInTwoWays(1.6, 1.6, 900000000, 1, 299792458, 10000, 2.5, 30, 3)
