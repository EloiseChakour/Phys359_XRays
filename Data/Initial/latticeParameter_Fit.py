# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:14:16 2021

@author: elois
"""

import numpy as np
import spinmob as s


#From Lorentzian
angles = np.array([21.7129, 25.273, 45.037, 47.652])#Peak positions
angle_errors = np.array([0.0007, 0.002, 0.004, 0.007])#From fitting the peak positions


#Sum of the Squares of the Mills Indices
integers = np.array([3.0, 4.0, 11.0, 12.0])



f=s.data.fitter(plot_guess = False, ylabel = "Angle (degrees)", xlabel = "Sum of the Squares of the Miller Indices")

#Fit Function for putting the "Integers" on the x-axis
f.set_functions(' arcsin((1.54*sqrt(x))/(2.0*a)) ','a = 3.6')

#Fit Function for putting the Angles on the x-axis
#f.set_functions('  (a**2)*(4.0/1.54**2)*sin(radians(x))**2','a = 3.6')

f.set_data(integers,angles, angle_errors)
values = f.get_fit_values()
f.fit()