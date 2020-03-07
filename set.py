# Initialising A Set

empty_Set = {}
fruits = {'Apple', 'Banana', 'Mango', 'Orange'}
print("\n\nSet of Fruits: ", fruits, "\n\n")

# Adding items to a set
## Single item

fruits.add("Strawberry")
print("After Adding Strawberry: ", fruits)

## Multiple Items

fruits.update(["Strawberry","Grapes","Papaya"])
print("After Inserting Multiple  fruits: ", fruits, "\n\n")

# Removing Items

print("Before Removing: ", fruits)
fruits.remove("Grapes")
print("After Removing Grapes: ", fruits, "\n")

# Getting the length of a Set

no_of_fruits = len(fruits)
print("Number of fruits: ", no_of_fruits, "\n\n")

# Intersection of two Set

fruits_2 = {"Apple", "Mango", "Watermelon"}
print("Fruits 2: ",fruits_2)
common_fruits = fruits.intersection(fruits_2)
print("Common fruits: ", common_fruits, "\n\n")

# Combining two Set

vegetables = {"Spinach", "Onion", "Cucumber"}
print("Vegetables: ",vegetables)
all_food = fruits.union(vegetables)
print("Combined food: ", all_food, "\n\n")

# Deleting a Set

del vegetables

