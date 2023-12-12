import matplotlib.pyplot as plt
import numpy as np 
def my_hyperbolaa(a=1, b=1, c=0):
    x = np.arange(0.01, 10, 0.01)
    y = 1/x
 
    plt.plot(x, y, label='Andreya parabola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('Hyperbola')
    plt.legend()
if __name__ == '__main__':
	my_hyperbolaa()
          
def my_hyperbola(a=-1, b=-1, c=0):
    x = np.arange(-0.01, -10, 0.01)
    y = 1/x
    plt.savefig('lab_2.png')
if __name__ == '__main__':
	my_hyperbola()    