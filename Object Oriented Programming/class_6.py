class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@1992.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("Ali", "Usman", 50000)
emp2 = Employee("Furqan", "Azhar", 20000)

print(emp1.pay)
emp1.apply_raise()

print(emp1.pay)
