from fourier_data import fourierSeries 
import numpy as np
import matplotlib.pyplot as plt


func_directory = { 'Square':   lambda x: x/np.abs(x)}
expansion = 49
f = fourierSeries(function_name='Square',function_directory=func_directory,num_expansion=expansion)
f = f.fourier_series_info()
plt.subplot()
plt.plot(f[0],f[1])
plt.plot(f[0],f[2])
plt.plot(f[0],f[3])
print(f[4])
plt.show()
#print(f)


 