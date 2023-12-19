import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

	
def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 2)
    x = x0 + R*alpha-np.sin(alpha)
    y = y0 + R*alpha-np.cos(alpha)
    return x, y
 
 
def animate(i):
    ball.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))
 
 
	
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='r', label='Ball')
 
    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30
                       )
 
    ani.save('lab7.1.gif') 
