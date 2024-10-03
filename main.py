import pandas as pd

# data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# series = pd.Series(data)
# print(series)

# data = {
#     'Name': ['Alice', 'Bob', 'Claire', 'John'],
#     'Age': [25, 30, 27, 35],
#     'City': ['New York', 'Paris', 'London', 'Tokyo']
# }
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('data.csv')
# print(df[['Country name', 'Regional indicator', 'Ladder score']])
print(df[df['Healthy life expectancy'] > 0.7])