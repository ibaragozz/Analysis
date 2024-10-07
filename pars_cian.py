import csv

# Имя исходного и нового файла
input_file = 'prices.csv'
output_file = 'cleaned_prices.csv'


# Функция для удаления символов и преобразования строки в число
def clean_price(price_str):
    # Убираем символ рубля и пробелы
    price_str = price_str.replace('₽', '').replace(' ', '')
    # Преобразуем в число (в целое или с плавающей точкой)
    try:
        return int(price_str)
    except ValueError:
        return float(price_str)


# Чтение исходного CSV и запись очищенных данных в новый CSV файл
with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Чтение заголовка и запись его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обработка строк с ценами
    for row in reader:
        # Очищаем цену в строке
        cleaned_price = clean_price(row[0])  # Предполагается, что цена в первом столбце
        writer.writerow([cleaned_price])

print(f"Очищенные данные сохранены в {output_file}")
