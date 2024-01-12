import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

	
def circle_move(R):
    alpha = np.arange(0, 2.5*np.pi, 0.1)
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x, y
 
 
def animate(R):
    ball.set_data(circle_move(R))
 
 
	
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='b', label='Ball')
 
    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 3, 0.1),
                        interval=30
                       )
 
    ani.save('a.gif') 
