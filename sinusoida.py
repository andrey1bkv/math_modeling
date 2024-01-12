import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots() 
 
anim_object, = plt.plot([], [], '-', lw=1) 
 
xdata, ydata = [], [] 

ax.set_xlim(0, 8*np.pi)  
ax.set_ylim(-2, 2) 
#
def update(frame):
    xdata.append(frame) 
    ydata.append(np.sin(frame))
    anim_object.set_data(xdata, ydata) 
    return anim_object
 
ani = FuncAnimation(fig,
                    update, 
                    frames=np.arange(0, 8*np.pi, 0.2),
                    interval=50 
                    )            
 
ani.save('sinusoida.gif')