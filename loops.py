# FOR LOOP

## List, Tuple, Set
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print("\n")

## String
for x in "banana":
    print(x)
print("\n")

## Range function

for x in range(6):
    print(x)
print("\n")

for x in range(2,9):
    print(x)
print("\n")

## Nested Loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
print("\n")

# WHILE LOOP

i = 1
while i < 6:
    print(i)
    i += 1
print("\n")

# Break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print("\n")

# Continue Statement

for x in fruits:
    if x == "banana":
        continue
    print(x)
print("\n")