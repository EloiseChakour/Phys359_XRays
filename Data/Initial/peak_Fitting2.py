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


a=1675
b=1745

x_short = x[a:b]
y_short = y[a:b]



f=s.data.fitter()
f.set_functions('a * (0.5*g)/((x-2.0*b)**2 + (0.5*g)**2)','a = 120, b=45, g = 1.0')
#Gaussian Function with guessed value for parameter a,b,c,d, and e 
#f.set_functions('(a/(c * sqrt(2 * pi)))* exp(-0.5* (x - b)2/(c2)) + d(-0.043x + 20.35 - 1.36*erf(x-b))','a=1873, b=276.8, c=13.8 , d=2.0')
#f.set_data(x,y, np.sqrt(y))
f.set_data(x_short,y_short, np.sqrt(y_short))
values = f.get_fit_values()
f.fit()
