while True:

    number = int(input("Please Enter the Table you want to print: "))

    for i in range(1,11):
        print(number, "x", i, "=", number*i)