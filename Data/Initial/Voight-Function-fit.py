# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:27:14 2021

@author: 
"""

import numpy as np
import matplotlib.pyplot as plt
from lmfit.models import GaussianModel, VoigtModel, LinearModel, ConstantModel

x = np.arange(13)
xx = np.linspace(0, 13, 100)
y = np.array([19699.959 , 21679.445 , 21143.195 , 20602.875 , 16246.769 ,
              11635.25  ,  8602.465 ,  7035.493 ,  6697.0337,  6510.092 ,
              7717.772 , 12270.446 , 16807.81  ])

# build model as Voigt + Constant
## model = GaussianModel() + ConstantModel()
model = VoigtModel() + ConstantModel()

# create parameters with initial values
params = model.make_params(amplitude=-1e5, center=8, 
                           sigma=2, gamma=2, c=25000)

# maybe place bounds on some parameters
params['center'].min = 2
params['center'].max = 12
params['amplitude'].max = 0. 

# do the fit, print out report with results 
result = model.fit(y, params, x=x)
print(result.fit_report())

# plot data, best fit, fit interpolated to `xx`
plt.plot(x, y, 'b+:', label='data')
plt.plot(x, result.best_fit, 'ko', label='fitted points')
plt.plot(xx, result.eval(x=xx), 'r-', label='interpolated fit')
plt.legend()
plt.show()