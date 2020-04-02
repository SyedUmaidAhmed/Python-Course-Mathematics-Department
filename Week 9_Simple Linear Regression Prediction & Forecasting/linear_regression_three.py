import pandas as pd
import numpy as np
from sklearn import linear_model

df =pd.read_csv('canada_economy.csv')

reg = linear_model.LinearRegression()

reg.fit(df[['year']], df.income)

print(reg.predict([[2020]]))