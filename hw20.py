import pandas as pd

data = pd.read_csv('dz.csv')

print(data.head())
print(data.info())
print(data.describe())
group = data.groupby('City')['Salary'].mean()
print(group)
