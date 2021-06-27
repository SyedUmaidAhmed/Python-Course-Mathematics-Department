class Vehicle:   #parent class
  "Parent Class"
  def __init__(self, price):
    self.price = price
  def display(self):
    print ('Price = $',self.price)

class Category(Vehicle):   #derived class
   "Child/Derived class"
   def __init__(self, price, name):
     Vehicle.__init__(self, price)
     self.name = name

   def disp_name(self):
     print ('Vehicle = ',self.name)

obj = Category(1200, 'BMW')
obj.disp_name()
obj.display()
