import numpy as np
import matplotlib.pyplot as plt

# Задание №1

data = np.random.normal(0,1,1000)
plt.hist(data)
plt.show()

# Задание №2

x = np.random.rand(5)
y = np.random.randn(5)
plt.scatter(x, y)
plt.show()
