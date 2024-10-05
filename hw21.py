import pandas as pd

data = {
    "Имя": ["Алексей", "Мария", "Иван", "Сергей", "Ольга", "Дмитрий", "Анна", "Екатерина", "Михаил", "Наталья"],
    "Математика": [3, 5, 4, 4, 3, 2, 5, 4, 5, 4],
    "Физика": [4, 5, 3, 3, 4, 3, 5, 4, 3, 4],
    "Химия": [5, 4, 4, 3, 4, 2, 5, 5, 4, 3],
    "История": [3, 4, 3, 5, 4, 3, 5, 4, 5, 4],
    "Литература": [4, 5, 5, 3, 4, 4, 5, 5, 3, 5]
}

df = pd.DataFrame(data)

print(f'Средняя оценка по каждому предмету: \n{df.mean(numeric_only=True)}')

print(f'Медианная оценка по каждому предмету: \n{df.median(numeric_only=True)}')


Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)

print(f'Квартили Математика: {Q1_math} и {Q3_math}')

IQR_math = Q3_math - Q1_math
downside_math = Q1_math - 1.5 * IQR_math
upside_math = Q3_math + 1.5 * IQR_math

print(f'Нижняя граница Математика: {downside_math}')
print(f'Верхняя граница Математика: {upside_math}')

print(f'Стандартное отклонение - {df["Математика"].std()}')


