# basics
def basic():
    """This function prints
    hello world"""
    print("hello world")


# syntax and declaration
def greet(name):
	print("Hello, " + name + "!")


# return
def square(x):
    return x * x


# variable arguments
def add(x, y):
    z = x + y
    print("The result of addition is: " + str(z))

# default arguments
def simple_interest(p=1000, r=5, t=1):
    si = (p * r * t) / 100.0
    print("The simple interest is: Rs. " + str(si))

# arbitrary arguments
def introduce_team(*names):
    for name in names:
       print("Hello", name)

# kwargs
def speak(sound1, sound2):
    print("Dog says {} and cat says {}".format(sound1, sound2))


# scope and lifetime
def my_func():
    print("value of a inside the function:", a)
    # global a
    # a = 10
    # print("value of a inside the function:", a)


if __name__ == '__main__':
    basic()

    # greet("Jake Peralta")

    # add(2, 4)

    # simple_interest(2000, 3, 8)
    
    # introduce_team("Richard", "Gilfoyle", "Dinesh", "Jared")

    # speak("bhow", "meow")
    # speak("meow", "bhow")
    # speak(sound2="meow", sound1="bhow")

    # val = square(3)
    # print("Squared value is: {}".format(val))

    a = 20
    # my_func()
    # print("value of a outside the function:", a)