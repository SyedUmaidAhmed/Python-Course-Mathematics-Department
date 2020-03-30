def AP(x,y):
    area = x*y
    perimeter = 2*x + 2*y
    print("The area of given rectangle is: ", area)
    print("The perimeter of given rectangle is: ", perimeter)

while True:
    a = int(input("Enter the length of rectangle side: "))
    b = int(input("Enter the breadth of rectangle side: "))
    AP(a,b)