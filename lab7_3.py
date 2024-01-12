import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots() 
 
anim_object, = plt.plot([], [], '', lw=2)

xdata, ydata = [], [] 
 
ax.set_xlim(0, 2*np.pi) 
ax.set_ylim(-1, 1)
 

def update(alpha):
    xdata.append(16*np.sin(alpha)*np.sin(alpha)*np.sin(alpha))
    ydata.append(13*np.cos(alpha)-5*np.cos(2*alpha)-2*np.cos(3*alpha)-np.cos(3*alpha))
    anim_object.set_data(xdata, ydata) 
    return anim_object,
 
ani = FuncAnimation(fig, 
                    update,
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=200
                    )            
ani.save("ddswd.gif") 