# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:14:16 2021

@author: elois
"""

import numpy as np
import spinmob as s

#From Gaussians
#angles = np.array([21.7139, 25.277, 45.040, 47.652])
#angle_errors = np.array([0.0008, 0.002, 0.004, 0.006])

#From Lorentzian
angles = np.array([21.7129, 25.273, 45.037, 47.652])
angle_errors = np.array([0.0007, 0.002, 0.004, 0.007])




d = (1.54)/(2.0* np.sin(np.radians(angles)))

mills = 1.0/(d**2.0)

factor = mills[0]/3.0

"""
print(factor)
print(d)
print(mills)
print(mills/factor)
"""
integers = np.array([3.0, 4.0, 11.0, 12.0])
errors = integers - (mills/factor) + 0.0001
#sqrtint = np.sqrt(integers)

test = np.arcsin((1.54*np.sqrt(integers))/(2*3.6))


#f=s.data.fitter(plot_guess = False, xlabel = "Angle (degrees)", ylabel = "Sum of the Squares of the Mills Indices")
f=s.data.fitter(plot_guess = False, ylabel = "Angle (degrees)", xlabel = "Sum of the Squares of the Miller Indices")
#f=s.data.fitter()
#f.set_functions(' (1.0/a)*arcsin((1.54*sqrt(x))/(2.0)) ','a = 3.6')
f.set_functions('  (a**2)*(4.0/1.54**2)*sin(radians(x))**2','a = 3.6')
f.set_data(angles,integers, errors)
values = f.get_fit_values()
f.fit()
