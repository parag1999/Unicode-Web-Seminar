#inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

p1 = Person("John", "Doe")
p1.printname()


class Student(Person):
  def __init__(self, fname, lname, graduation_year):
    super().__init__(fname, lname)# use super() method to inherit all the properties and the methods of the parent class
    self.graduation_year = graduation_year

s1 = Student("Mike", "Olsen", 2021)
print(s1.firstname,s1.lastname,s1.graduation_year)
s1.printname()