import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
sin_dict={ 'S1':[2,5],
           'S2':[5,10],
           'S3':[3,7],
           'S4':[10,12],
           'S5':[1,2],}
k=input ('Enter sinusoidal key to generate')
if sin_dict[k]:
	x=sin_dict[k][0]*np.sin(2*np.pi*sin_dict[k][1]*t)
	plt.plot(t,x)
	plt.show()
           
           
