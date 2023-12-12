import matplotlib.pyplot as plt

x = [3, 4, 5, 1]
y = [2, 9, 7, 1]

plt.plot(x, y, color ='g', label = 'Graf 1', marker '>', ms = 5)
plt.plot(x, y, color ='p', label = 'Graf 2', marker 'o', ms = 3)

plt.savefig('fig_2.png')