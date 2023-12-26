import matplotlib.pyplot as plt
import numpy as np 
def ellips_plotter(a=1, b=2,):
    x = np.arange(-10, 10,)
    y = 1-x*b/a

    plt.plot(x, y, label='Andreya ellips')
    plt.title('Ellips')
    plt.legend() 
    plt.savefig('lab_3.png')  

if __name__ == '__main__':      
	ellips_plotter
                




