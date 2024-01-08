import matplotlib.pyplot as plt
import numpy as np

def cicloida_plotter(R=10):
    
    alpha = np.arange(0, 2*np.pi, 0.01)
    
    
    #x = R * (alpha - 0,25 * (3*np.sin(alpha) - np.sin(3*alpha)))
    #y = R * (1 - 0,25 * (3*np.cos(alpha) - np.cos(3*alpha)))
    
    x = R * (alpha - (np.sin(alpha)*np.sin(alpha)*np.sin(alpha)))
    y = R * (1 - (np.cos(alpha)*np.cos(alpha)*np.cos(alpha)))
    
    plt.plot(x, y, ls='-', lw=5)
    
    plt.savefig('lab777.png')

if __name__ == '__main__':
	cicloida_plotter()    