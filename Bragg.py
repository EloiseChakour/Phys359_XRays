# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:14:16 2021

@author: elois
"""

import numpy as np
import spinmob as s


#Sn, with alpha1 only 
angles1 = np.array([15.3608, 22.0066, 27.7068, 31.3068, 31.9391, 32.3351, 36.234, 36.6221, 39.7914, 44.7443])
angle_errors1 = np.array([0.0015, 0.0014, 0.0037, 0.0034, 0.0072, 0.0038, 0.0027, 0.0052, 0.0037, 0.0041])

#Sn, with alpha2 only 
angles2 = np.array([16.0584, 22.5072, 27.7985, 31.3894, 32.022, 32.4349, 36.3384, 36.7301, 39.9083, 44.8902])
angle_errors2 = np.array([0.0012, 0.0017, 0.0037, 0.0059, 0.014, 0.0071, 0.0038, 0.0088, 0.0059, 0.0059])


#Sn, with weighted average
angles = (2* angles1 + angles2)/3.0
angle_errors = angle_errors1 + angle_errors2

#K averaged
d_Ave = (1.541838)/(2.0* np.sin(np.radians(angles)))


#K alpha1
d1 = (1.540562)/(2.0* np.sin(np.radians(angles1)))


#K alpha2
d2 = (1.544390)/(2.0* np.sin(np.radians(angles2)))

mills = 1.0/(d_Ave**2.0)

factor = mills[0]/3.0


print(factor)
print(d_Ave)
print(mills)
print(mills/factor)



#f=s.data.fitter(plot_guess = False, xlabel = "Angle (degrees)", ylabel = "Sum of the Squares of the Mills Indices")
f=s.data.fitter(plot_guess = False, ylabel = "Angle (degrees)", xlabel = "Sum of the Squares of the Miller Indices")
#f=s.data.fitter()
#f.set_functions(' (1.0/a)*arcsin((1.54*sqrt(x))/(2.0)) ','a = 3.6')
f.set_functions('  (a**2)*(4.0/1.54**2)*sin(radians(x))**2','a = 3.6')
f.set_data(angles,integers, errors)
values = f.get_fit_values()
f.fit()
