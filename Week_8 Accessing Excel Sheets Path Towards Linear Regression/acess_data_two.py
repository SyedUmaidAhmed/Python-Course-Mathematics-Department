import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('homeprice.csv')
print(df)

plt.xlabel('Area')
plt.ylabel('Prices')

plt.scatter(df.area, df.price, color='blue', marker='+')
plt.show()