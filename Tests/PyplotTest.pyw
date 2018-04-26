from matplotlib import pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
##a=np.arange(-2*np.pi,2*np.pi,step=np.pi/50)
##pyplot.plot((np.sin(a)/a)**2,'b-')#,np.cos(a)/2+1)
##pyplot.plot(np.cos(a)/2+1)
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
a=np.arange(-2,2,step=1/50)
b=0.5
l,= plt.plot(a,b*np.cosh(a/b), color='red')
plt.axis([-1, 1, 0,20])

axcolor = 'lightgoldenrodyellow'
axb = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

sb = Slider(axb, 'b', 0.1, 1, valinit=b)#, valstep=delta_f)

def update(val):
    b = sb.val
    l.set_ydata(b*np.cosh(a/b)-b)
    fig.canvas.draw_idle()
sb.on_changed(update)


##plt.plot(a,b*np.cosh(a/b))
##plt.xlabel('Real Number')
plt.show()
