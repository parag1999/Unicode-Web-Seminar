class Person:
    def __init__(self,name,age): # a factory method that constructs an object of the class first parameter to this is always the object reference.
        self.name = name # not necessary to use self as the name of the variable, go ahead and change it to mysillyname or somestupidshit.
        self.age = age # remember to change the name everywhere in the init function.

    def sayName(self,greet=True):
        if greet:
            print("Hello my name is " + self.name)
        else:
            print(self.name)

p1 = Person("Rosa",23)
print(p1.name)

p2 = Person("Eddy",24)
p3 = Person("Parag",21)
p4 = Person("Siddharth",21)

print(p1.name + "'s friends are " + p2.name + ", " + p3.name + " and " + p4.name + ".")

print("Their ages are " + str(p2.age) + ", " + str(p3.age) + " and " + str(p4.age) + ".")

p1.sayName()
p2.sayName(greet=False)
p3.sayName(greet=False)
p4.sayName()