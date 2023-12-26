import matplotlib.pyplot as plt
import numpy as np 
def ellips_plotter(a=150, b=90):
     x = a*cos(t)
     y = b*sin(t)
     x = np.arange(10, -10)
     x = np.arange(20, -20)
     plt.plot(x, y, label='Andreya ellips')
     plt.title('Ellips')
     plt.legend() 
     plt.savefig('lab_3.png')  

if __name__ == '__main__':      
	ellips_plotter
                




