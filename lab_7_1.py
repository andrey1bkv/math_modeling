import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def cicloida_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.01)
    #x = R * (alpha - 0,25 * (3*np.sin(alpha) - np.sin(3*alpha)))
    #y = R * (1 - 0,25 * (3
    *np.cos(alpha) - np.cos(3*alpha)))
    
    return x, y

def animate(i):
    ball.set_data(cicloida_move(R=1, vx0=0.05, vy0=0.05, time=i))
 
 
	
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='r', label='Ball')
 
    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=320,
                        interval=30
                       )
 
    ani.save('lab_7_1.gif')   
    
def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.01)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y


 
 
def animate(i):
    ball.set_data(circle_move(R=1, vx0=0.001, vy0=0.01, time=i))
 
 
	
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='r', label='Ball')
 
    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=320,
                        interval=30
                       )
 
    ani.save('lab_7_1.gif') 
    
    




    
