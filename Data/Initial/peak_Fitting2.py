# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:48:47 2021

@author: elois
"""
import spinmob as s
#import mcphysics as mcp
#import matplotlib.pyplot as plt
import numpy as np





file  = open("Cu_03-09-20.uxd", "r") 
#file  = open("Ni_03-09-20.uxd", "r") 

#file  = open("Cu25Ni75.uxd", "r") 
#file  = open("Cu50Ni50.uxd", "r") 
#file  = open("Cu75Ni25.uxd", "r") 

#file  = open("Pb_08-09-20D.uxd", "r") 
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

for i in range(len(y)):
    if y[i] ==0:
        y[i] = 1.0


file.close()


a=650
b=690

x_short = x[a:b]
y_short = y[a:b]



f=s.data.fitter(plot_guess= False)
f.set_functions('a * (0.5*g)/((x-2.0*b)**2 + (0.5*g)**2) + c*exp(-(x-2.0*b)**2/(2*g**2)) + z','a = 50, b=21.7, g = 0.14, c = 800, z=12')
#Gaussian Function with guessed value for parameter a,b,c,d, and e 
#f.set_functions('(a/(c * sqrt(2 * pi)))* exp(-0.5* (x - b)2/(c2)) + d(-0.043x + 20.35 - 1.36*erf(x-b))','a=1873, b=276.8, c=13.8 , d=2.0')
#f.set_data(x,y, np.sqrt(y))
f.set_data(x_short,y_short, np.sqrt(y_short))
values = f.get_fit_values()
f.fit()
