# Only If Condition
a = 33
b = 200
if b > a:
    print("b is greater than a\n")

# If, Else if and else condition
c = 33
d = 33
if c > d:
    print("d is greater than c\n")
elif c == d:
    print("c and d are equal\n")
else:
    print("c is greater than d\n")

# Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!\n")
  else:
    print("but not above 20.\n")


a = 200
b = 33
c = 500
# And keyword
if a > b and c > a:
    print("Both conditions are True\n")
# Or keyword
if a > b or a > c:
    print("At least one of the conditions is True\n")


# IF Statements in different collections
## List, Tuple or Set

fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list\n")

fruits = ("apple", "banana", "cherry")
if "mango" not in fruits:
  print("No, 'mango' is not in the fruits tuple\n")

## Dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary\n")
