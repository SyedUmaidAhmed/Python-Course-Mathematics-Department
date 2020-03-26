from functools import reduce

list1 =[2,4,5,12,18]

c = reduce(lambda x,y: x+y, list1)

print(c)

# 2+4 =6, 6+5=11,...11+12