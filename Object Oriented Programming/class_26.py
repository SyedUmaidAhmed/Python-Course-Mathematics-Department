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

    


dev1 = Developer("Ahmed", "Usman", 50000, 'Python')
dev2 = Developer("Furqan", "Asad", 60000,'C++')

print(dev1.email)
print(dev1.prog_lang)
