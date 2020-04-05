     ############# LEVEL 0 ##############
### 1) Import libraries (pandas, numpy, matplotlib, seaborn, statsmodel)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

### 2) Import data
df = pd.read_csv("data.csv")
print(df)
#
# ### 3) Shape of data
print(df.shape)
#
# ### 4) How data looks in tabular form
print(df.head(10))
#
# ### 6) Name of columns in data
print(df.columns)
#
# ### 7) Data types (int or float)
print(df.dtypes)
#
# ### 8) Drop unimportant columns
column = ['X1 transaction date','X3 distance to the nearest MRT station','X4 number of convenience stores','X5 latitude','X6 longitude']
df = df.drop(column, axis = 1)
print(df)
### 9) mean, median, standard deviation, min, max values of data
print("Mean", df.mean())
print("Median", df.median())
print("min", df.min())
print("max", df.max())
print("standard deviation", df.std())

print(df.describe())

     ############# LEVEL 1 ##############

### 1) Scatter plot of data
plt.figure(figsize= (10,7))
sns.scatterplot(x = "X2 house age", y = "Y house price of unit area", data = df)

### 2) Distribution plot of data
plt.figure(figsize= (10,7))
sns.distplot( df["Y house price of unit area"])
plt.show()

### 3) Simple Linear Regression for R-square and p-value
x = df["X2 house age"]
y = df["Y house price of unit area"]

model = sm.OLS(y,x).fit()

print(model.rsquared)
print(model.pvalues)

print(model.summary())
