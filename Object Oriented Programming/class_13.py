class Employee:
    
    no_of_emps= 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@1992.com'

        Employee.no_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

emp1 = Employee("Ali", "Usman", 50000)
emp2 = Employee("Furqan", "Azhar", 20000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Coel-Tom-10000'
emp_str_3 = 'Smith-Aan-50000'

first,last,pay = emp_str_1.split('-')
new_emp_1 = Employee(first,last,pay)
print(new_emp_1.email)
print(new_emp_1.pay)
