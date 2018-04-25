from matplotlib import pyplot
import numpy as np
a=np.arange(-2*np.pi,2*np.pi,step=np.pi/50)
pyplot.plot((np.sin(a)/a)**2,'b-')#,np.cos(a)/2+1)
pyplot.plot(np.cos(a)/2+1)
pyplot.xlabel('Real Number')
pyplot.show()
