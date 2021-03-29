# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:14:16 2021

@author: elois
"""

import numpy as np
import spinmob as s


#From Voight, Copper
#angles = np.array([21.7136, 25.274, 37.128, 45.036, 47.651])
#angle_errors = np.array([0.0007, 0.002, 0.003, 0.004, 0.007])


#Nickel, Voight
#angles = np.array([22.2942, 25.969, 38.247, 46.530, 49.276])
#angle_errors = np.array([0.0008, 0.002, 0.003, 0.004, 0.008])

#From Voight, Cu25Ni75
#angles = np.array([22.162, 25.818, 38.000, 46.196, 48.91])
#angle_errors = np.array([0.001, 0.003, 0.004, 0.007, 0.01])


#Cu50Ni50, Voight
#angles = np.array([22.031, 25.653, 37.737, 45.854, 48.57])
#angle_errors = np.array([0.001, 0.003, 0.005, 0.007, 0.01])


#Pb, with alpha1 only 
angles1 = np.array([15.6942, 18.189, 26.184, 31.149, 32.660, 38.535, 42.755, 44.136, 49.725, 54.008])
angle_errors1 = np.array([0.0007, 0.001, 0.002, 0.002, 0.002, 0.005, 0.004, 0.003, 0.007, 0.005])

#Pb, with alpha2 only 
angles2 = np.array([15.6942, 18.189, 26.184, 31.149, 32.742, 38.652, 42.886, 44.277, 49.89, 54.193])
angle_errors2 = np.array([0.0007, 0.001, 0.002, 0.002, 0.002, 0.009, 0.006, 0.005, 0.01, 0.008])


#Pb, with weighted average
angles = (2* angles1 + angles2)/3.0
angle_errors = angle_errors1 + angle_errors2

# =============================================================================
# #K averaged
# d = (1.541838)/(2.0* np.sin(np.radians(angles)))
# =============================================================================

# =============================================================================
# #K alpha1
# d = (1.540562)/(2.0* np.sin(np.radians(angles1)))
# =============================================================================

#K alpha2
d = (1.544390)/(2.0* np.sin(np.radians(angles2)))

mills = 1.0/(d**2.0)

factor = mills[0]/3.0


print(factor)
print(d)
print(mills)
print(mills/factor)


"""
#f=s.data.fitter(plot_guess = False, xlabel = "Angle (degrees)", ylabel = "Sum of the Squares of the Mills Indices")
f=s.data.fitter(plot_guess = False, ylabel = "Angle (degrees)", xlabel = "Sum of the Squares of the Miller Indices")
#f=s.data.fitter()
#f.set_functions(' (1.0/a)*arcsin((1.54*sqrt(x))/(2.0)) ','a = 3.6')
f.set_functions('  (a**2)*(4.0/1.54**2)*sin(radians(x))**2','a = 3.6')
f.set_data(angles,integers, errors)
values = f.get_fit_values()
f.fit()
"""