import matplotlib.pyplot as plt

# x = [2,6,8,14,20]
# y = [6,4,10,12,16]
#
# plt.plot(x, y)
#
# plt.title('Пример простого линейного графика')
# plt.xlabel('x ось')
# plt.ylabel('y ось')
#
# plt.show()

# data = [1,2,2,3,4,4,4,5,6,6,6,6,6]
#
# plt.hist(data, bins=6)
# plt.xlabel('x ось')
# plt.ylabel('y ось')
# plt.title('Пример гистограммы')
#
# plt.show()

x = [1,4,6,7]
y = [3,5,8,10]
plt.scatter(x, y)
plt.xlabel('x ось')
plt.ylabel('y ось')
plt.title('Пример диаграммы рассеяния')

plt.show()