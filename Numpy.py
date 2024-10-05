import pandas as pd
import numpy as np


date = pd.date_range(start='2022-07-26', periods=10, freq='D')
values = np.random.rand(10)

df = pd.DataFrame({'Date': date, 'values': values})
df.set_index('Date', inplace=True)

print(df)

month = df.resample('ME').mean()

print(month)