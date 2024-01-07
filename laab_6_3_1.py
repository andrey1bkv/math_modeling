import matplotlib.pyplot as plt
import numpy as np 

def ellips_plottrer(a=10, b=10):

    x = 
    y =

    X, Y = np.meshgrid(x, y)

    fxy = 1 - Y**2 / b**2 * a**2 

    plt.contour( X, Y, fxy, levels = [0])
    plt.axis('equal') 

    plt.savefig('lab3.png')
    
if __name__ == '__main__':
	ellips_plottrer()