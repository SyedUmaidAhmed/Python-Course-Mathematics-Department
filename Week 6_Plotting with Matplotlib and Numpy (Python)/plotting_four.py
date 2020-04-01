import matplotlib.pyplot as plt


year=[1960,1970,1980,1990,2000,2010]
pop_pakistan=[44.91,58.09,78.07,107.7,138.5,170.6]
pop_india=[449.48,553.57,696.783,870.133,1000.4,1309.4]


plt.plot(year,pop_pakistan,color='g',label="PAKISTAN")
plt.plot(year,pop_india,color='orange',label='INDIA')

plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Comparison')
plt.show()