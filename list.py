# Initialising A List

empty_list = []
fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Papaya']
print("\n\nList of Fruits: ", fruits, "\n\n")

# Accessing Items In A List

print("The second fruit is: ", fruits[1])
print("The last fruit is: ", fruits[-1])
print("Fruits from second to fourth position: ", fruits[1:4])
print("Fruits from start to fourth position: ", fruits[:4])
print("Fruits from fourth position till the end: ", fruits[4:])
print("Fruits from fourth last to second last position: ", fruits[-4:-1],"\n\n")

# Changing Item Value

print("Before Changing second fruit: ", fruits)
fruits[1] = "Grapes"
print("After Changing second fruit: ", fruits, "\n\n")

# Adding items to a list
## Using append

print("Before Adding: ", fruits)
fruits.append("Banana")
print("After Adding Banana: ", fruits)

## Using insert

fruits.insert(3, "Strawberry")
print("After Inserting Strawberry at fourth position: ", fruits, "\n\n")

# Removing Items
## Using remove

print("Before Removing: ", fruits)
fruits.remove("Grapes")
print("After Removing Grapes: ", fruits, "\n")

## Using Pop

print("Before Popping: ", fruits)
fruits.pop()
print("By Default Pop: ", fruits)
fruits.pop(1)
print("After Popping second fruit: ", fruits, "\n\n")

# Copying a list

fruits_copy = fruits.copy()
print("Copy of Fruits: ", fruits_copy, "\n\n")

# Clearing a list

fruits_copy.clear()
print("Emptied list: ", fruits_copy, "\n\n")

# Deleting a list

del fruits_copy
#print("Deleted list: ", fruits_copy)

# Getting the length of a list

no_of_fruits = len(fruits)
print("Number of fruits: ", no_of_fruits, "\n\n")

# Combining two list
## Using operators

vegetables = ["Spinach", "Onion", "Cucumber"]
print("Vegetables: ",vegetables)
all_food = fruits + vegetables
print("Combined food: ", all_food)
## Using extend

fruits.extend(vegetables)

print("Adding vegetables to fruits: ", fruits, "\n\n")