import matplotlib.pyplot as plt
x = [1, 1, 5, 5, 1]
y = [1, 5, 5, 1, 1]

plt.plot(x, y, color='k', marker='*', ms='10')
plt.axis('equal')

plt.savefig('lab_1.png')

