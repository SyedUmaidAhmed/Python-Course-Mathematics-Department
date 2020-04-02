import pandas as pd
import numpy as np
from sklearn import linear_model

df =pd.read_csv('homeprice.csv')

reg = linear_model.LinearRegression()

reg.fit(df[['area']], df.price)

print(reg.predict([[3300]]))