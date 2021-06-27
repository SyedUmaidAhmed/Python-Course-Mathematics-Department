class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@1992.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee("Ali", "Usman", 50000)
emp2 = Employee("Furqan", "Azhar", 20000)


print(emp1.fullname())
print(emp2.fullname())
