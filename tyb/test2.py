#%%
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x = np.arange(-2*np.pi, 2*np.pi, 0.02)
y1 = np.sin(x)
y2 = np.cos(x)

figure(figsize=(10,6), dpi=80)

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#刻度标签
xticks([-2*np.pi,-3*np.pi/2,-np.pi,-np.pi/2,0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],[r'$-2\pi$',r'$-3\pi/2$',r'$-\pi$',r'$-\pi/2$',r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$+2\pi$'])

plot(x,y1,color="red", linewidth=2.5, label="sin(x)")
plot(x,y2,color="blue", linewidth=2.5, label="cos(x)")
legend(loc='upper right')

show()
