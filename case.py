from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие страницы
url = "https://murmansk.cian.ru/kupit-2-komnatnuyu-kvartiru-vtorichka-murmanskaya-oblast-severomorsk/"
driver.get(url)

# Задержка для полной загрузки страницы
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Сохраняем данные в CSV файл
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок CSV файла

    # Записываем цены в файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()
