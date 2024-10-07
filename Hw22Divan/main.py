from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие страницы
url = "https://www.divan.ru/sankt-peterburg/category/divany-i-kresla"
driver.get(url)

# Задержка для полной загрузки страницы
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, '//span[@class="e1pugr3w0 css-10b17yd-StyledPrice e1pugr3w1"]')

# Сохраняем данные в CSV файл
with open('divan_prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок CSV файла

    # Записываем цены в файл
    for price in prices:
        price_text = price.text.replace('₽', '').replace(' ', '')  # Убираем символ рубля и пробелы
        writer.writerow([price_text])

# Закрытие драйвера
driver.quit()
