import matplotlib.pyplot as plt
x1 = [1,2,3]
y1 = [2,4,1]

plt.plot(x1,y1, label="line1")

x2 = [1,2,3]
y2 = [4,3,1]

plt.plot(x2,y2, label="line2")

plt.title('Two lines on the same graph')

plt.legend()

plt.show()
