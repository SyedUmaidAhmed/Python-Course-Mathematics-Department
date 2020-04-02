import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv('homeprice.csv')


reg = linear_model.LinearRegression()

reg.fit(df[['area']], df.price)


area_df = pd.read_csv('areas.csv')

p = reg.predict(area_df)

area_df['prices']=p

area_df.to_csv("Our Area Based Predictions.csv")
