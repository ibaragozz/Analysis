import pandas as pd
import matplotlib.pyplot as plt

data = {'value': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}

df = pd.DataFrame(data)

# df['value'].hist()

# df.boxplot(column='value')
# plt.show()
print(df.describe())
