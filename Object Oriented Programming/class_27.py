class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + 'last' +'@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{] {}'.format(self.first, self.last)


class Developer(Employee):
    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

    

class Manager(Employee):
    def __init__(self,first,last,pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev1 = Developer("Ahmed", "Usman", 50000, 'Python')
dev2 = Developer("Furqan", "Asad", 60000,'C++')



mgr_1 = Manager('Sue','Smith', 90000, [dev1])
print(mgr_1.email)
mgr_1.add_emp(dev2)
mgr_1.print_emps()




