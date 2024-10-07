import csv
import matplotlib.pyplot as plt

# Чтение данных из файла divan_prices.csv
prices = []

with open('divan_prices.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        prices.append(int(row[0]))  # Добавляем цены как целые числа

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Размер графика
plt.hist(prices, bins=20, edgecolor='black', alpha=0.7)  # Гистограмма с 20 столбцами
plt.title('Цены на диваны в Санкт-Петербурге')
plt.xlabel('Цена (₽)')
plt.ylabel('Кол-во товара')

# Отображение графика
plt.show()
