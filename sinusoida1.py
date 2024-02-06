import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

	
def circle_move(a, y0, phi, t):
    x = t
    y = y0 + a * np.sin(t + phi)
    return x, y
 
x1, y1 = [], []
x2, y2 = [], []
x3, y3 = [], []
def animate(t):
    coords1 = circle_move(1.2, 3, np.sin(t), t)
    x1.append(coords1[0])
    y1.append(coords1[1])
    sinus_1.set_data(x1, y1)

    coords2 = circle_move(2, 0, np.pi/2, t)
    x2.append(coords2[0])
    y2.append(coords2[1])
    sinus_2.set_data(x2, y2)

    x3.append(coords2[0])
    y3.append(coords2[1] + coords1[1]-6)
    sinus_3.set_data(x3, y3)
 
	
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    sinus_1, = plt.plot([], [], '-', color='r', label='sinus_1')
    sinus_2, = plt.plot([], [], '-', color='b', label='sinus_1')
    sinus_3, = plt.plot([], [], '-', color='g', label='sinus_1')
 
    edge = 5
    plt.axis('equal')
    ax.set_xlim(0, 30)
    ax.set_ylim(-6, 6)

    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(5, 28, 0.1),
                        interval=20
                       )
 
    ani.save('sinusoida5.gif') 








