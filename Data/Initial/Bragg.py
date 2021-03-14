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

#From Lorentzian, Copper
#angles = np.array([21.7129, 25.273, 45.037, 47.652])
#angle_errors = np.array([0.0007, 0.002, 0.004, 0.007])

#From Voight, Copper
angles = np.array([21.7136, 25.274, 37.128, 45.036, 47.651])
angle_errors = np.array([0.0007, 0.002, 0.003, 0.004, 0.007])


#Nickel, Lorentzian
#angles = np.array([22.2939, 25.967, 38.246, 46.530, 49.287])



#From Lorentzian, Cu25Ni75
#angles = np.array([22.161, 25.818, 37.998, 46.1982, 48.917])


d = (1.54)/(2.0* np.sin(np.radians(angles)))

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