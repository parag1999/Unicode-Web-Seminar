# class methods and static methods
class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    @classmethod # decorator which is a function which wraps the below function and performs a certain task, in this case pass the reference of the class as the first parameter
    def new_square(cls,side_length):
        return cls(side_length, side_length) #instantiating a new object of the class on which it was invoked
    
    @staticmethod #decorator that make the following function free of the class object reference and helps it perform various tasks without the need of creating the object
    def sayHello():
        print("hello I behave as a normal function and can do normal tasks and still belong to a class")

square = Rectangle.new_square(5)
print("area = ", square.calculate_area())
Rectangle.sayHello()