import numpy as np
import matplotlib.pyplot as plt

# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# b = np.zeros((3,3))
# c = np.ones((2,5))
# d = np.random.random((4,5))
# e = np.arange(0, 10, 2)
# f = np.linspace(0, 13, 10)
# g = np.full((3,3), 5)

x = np.linspace(-10, 10, 100)
y = x**2
plt.plot(x, y)
plt.xlabel('x ось')
plt.ylabel('y ось')
plt.title('График y = x^2')
plt.grid(True)

plt.show()