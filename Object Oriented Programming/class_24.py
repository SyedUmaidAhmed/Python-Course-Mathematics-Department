class Person:  
    name = ""  
    age = 0  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge
        
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  

class Student(Person):

    studentId = ""  
  
    def __init__(self, studentName, studentAge, studentId):  
        Person.__init__(self, studentName, studentAge)
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId
  
  
person1 = Person("Richard", 23)
person1.showAge()

student1 = Student("Max", 22, "102")
print(student1.getId())  
student1.showName()
