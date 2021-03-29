# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:57:05 2021

@author: elois
"""

import spinmob as s
#import mcphysics as mcp
#import matplotlib.pyplot as plt
import numpy as np
from scipy.special import wofz




#file  = open("Cu_03-09-20.uxd", "r") 
#file  = open("Ni_03-09-20.uxd", "r") 


#file  = open("Cu25Ni75.uxd", "r")
#file  = open("Cu50Ni50.uxd", "r") 
#file  = open("Cu75Ni25.uxd", "r") 

file  = open("Pb_08-09-20D.uxd", "r") 
#file  = open("Sn_08-09-20.uxd", "r") 



data = file.read()
data = data.split()

data_float = np.array(data)

x = []
y = []

for i in range(len(data_float)):
    if i == 0:
        x.append(float(data_float[i]))
    elif (i%2) == 0:
        x.append(float(data_float[i]))
    else:
        y.append(float(data_float[i]))

x = np.array(x)
y = np.array(y)


file.close()

for i in range(len(y)):
    if y[i] == 0:
        y[i] = 0.1


a=1480
b=1550

x_short = x[a:b]
y_short = y[a:b]



f=s.data.fitter(plot_guess=False)
f.set_functions('2*a * (0.5*g)/((x-2.0*b)**2 + (0.5*g)**2) + 2*a*exp(-(x-2.0*b)**2/(2*d**2))+ a * (0.5*g)/((x-2.0*h)**2 + (0.5*g)**2) + a*exp(-(x-2.0*h)**2/(2*d**2)) + z','a = 2, b=38.5,  g = 0.51, d = 0.1096, h=38.6, z=4')
#Gaussian Function with guessed value for parameter a,b,c,d, and e 
#f.set_data(x,y, np.sqrt(y))
f.set_data(x_short,y_short, np.sqrt(y_short))
values = f.get_fit_values()
f.fit()
