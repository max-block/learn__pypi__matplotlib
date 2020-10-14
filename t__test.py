import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)


def y(x):
    return [x * x for x in x]


plt.plot(x, y(x))
plt.show()
