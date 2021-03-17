# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:39:14 2021

@author: elois
"""

import numpy as np
import spinmob as s

percent_Ni = np.array([0.0, 0.25, 0.50, 0.75, 1.0])

latticeParam = np.array([3.6164, 3.5878, 3.5650, 3.5446, 3.5253])

latticeParamError = np.array([0.0003, 0.0004, 0.0005,0.0004, 0.0003])


f=s.data.fitter(plot_guess = False, ylabel = "Lattice Paramter (A)", xlabel = "Nickel to Copper Ratio")


#
f.set_functions(' a + (b-a)*x',' a=3.6164, b= 3.5253')

#W/ Our Values
#f.set_functions(' degrees(arcsin((1.541838*sqrt(x))/(2.0*(0.25*a + 0.75*b))))  + z','a = 3.6023, b=3.5253, z=1')


#Fit Function for putting the Angles on the x-axis
#f.set_functions('  (a**2)*(4.0/1.54**2)*sin(radians(x))**2','a = 3.6')

f.set_data(percent_Ni,latticeParam, latticeParamError)
values = f.get_fit_values()
f.fit()