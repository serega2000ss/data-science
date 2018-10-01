import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

## Create functions and set domain length
x = np.arange(0.0, 2.0, 0.01)
y = x**2
dy = 2*x - 1

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy)
plt.plot(1, 1, 'or')

## Config the graph
plt.title('A Cool Graph')
plt.xlabel('X')
plt.ylabel('Y')
#plt.ylim([0, 4])
plt.grid(True)
plt.legend(['y = x^2', 'y = 2x'], loc='upper left')

## Show the graph
plt.show()
