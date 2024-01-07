import matplotlib.pyplot as plt
import numpy as np 

def ellips_plottrer(a=1, b=2):
     
    x = np.arange(-2*a, 2*a, 0.1)
    y = np.arange(-2*b, 2*b, 0.1)


    X, Y = np.meshgrid(x, y)

    fxy = X**2 + Y**2 * a * b - 1

    plt.contour( X, Y, fxy, levels = [0]) 

    plt.axis('equal')
    plt.savefig('lab3.png')
    
if __name__ == '__main__':
	ellips_plottrer()