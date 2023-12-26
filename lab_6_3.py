import matplotlib.pyplot as plt
import numpy as np 
def ellips_plotter(a=1, b=1, c=0):
    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x