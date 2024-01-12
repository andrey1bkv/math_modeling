import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots()
 
anim_object, = plt.plot([], [], '-', lw=2) 
 
xdata, ydata = [], [] 
 
ax.set_xlim(0, 2*np.pi) 
ax.set_ylim(-1, 1)
 

def update(R=10):
    alpha = np.arange(0, 2*np.pi, 0.01)

    xdata.append(x = R * (alpha - (np.sin(alpha)*np.sin(alpha)*np.sin(alpha)))) 
    ydata.append(y = R * (1 - (np.cos(alpha)*np.cos(alpha)*np.cos(alpha)))) 
    anim_object.set_data(xdata, ydata)
    return anim_object,
 
ani = FuncAnimation(fig, # Стандартный вызов пространства
                    update, # Вызов функции подстановки координат
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=100 # Интервал между кадрами,
                    )            # по умолчанию 200 милисекунд
ani.save("рррррр.gif")