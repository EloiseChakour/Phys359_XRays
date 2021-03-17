# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:14:16 2021

@author: elois
"""

import numpy as np
import spinmob as s


#Copper, Voight
#angles = np.array([21.7136, 25.276, 37.128, 45.036, 47.651])
#angle_errors = np.array([0.0007, 0.002, 0.003, 0.004, 0.007])


#Nickel, Voight
#angles = np.array([22.2942, 25.969, 38.247, 46.530, 49.276])
#angle_errors = np.array([0.0008, 0.002, 0.003, 0.004, 0.008])

#Cu25NI75
#angles = np.array([22.162, 25.818, 38.000, 46.196, 48.91])
#angle_errors = np.array([0.001, 0.003, 0.004, 0.007, 0.01])



#Cu50Ni50, Voight
angles = np.array([22.031, 25.653, 37.737, 45.854, 48.57])
angle_errors = np.array([0.001, 0.003, 0.005, 0.007, 0.01])

#Sum of the Squares of the Mills Indices

#Copper
#integers = np.array([3.0, 4.0, 8.0, 11.0, 12.0])

#Nickel
#integers = np.array([3.0, 4.0, 8.0, 11.0, 12.0])


#Cu25Ni75
integers = np.array([3.0, 4.0, 8.0, 11.0, 12.0])



f=s.data.fitter(plot_guess = False, ylabel = "Angle (degrees)", xlabel = "Sum of the Squares of the Miller Indices")


#Fit Function for putting the "Integers" on the x-axis
f.set_functions(' degrees(arcsin((1.541838*sqrt(x))/(2.0*a))) + z','a = 3.58, z=1')

#Fit for Alloys with Vegard's Law
#f.set_functions(' degrees(arcsin((1.541838*sqrt(x))/(2.0*(0.25*a + 0.75*b))))  + z','a = 3.6023, b=3.5253, z=1')


#Fit Function for putting the Angles on the x-axis
#f.set_functions('  (a**2)*(4.0/1.54**2)*sin(radians(x))**2','a = 3.6')

f.set_data(integers,angles, angle_errors)
values = f.get_fit_values()
f.fit()