class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other): #the first parameter is the reference of the object before the + operetor and the other is the reference to the object after the + operator
        return Vector2D(self.x + other.x, self.y + other.y) # add the respective x's and y's of the vectors and return the new vector.

first = Vector2D(5,7)
second = Vector2D(3,9)

result = first + second # reference of first variable is passed as the first parameter and the reference of the second variable is passed as the second parameter.
print(result.x,result.y)