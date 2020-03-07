# Initialising A Tuple

empty_tuple = ()
fruits = ('Apple', 'Banana', 'Mango', 'Orange', 'Papaya')
print("\n\nTuple of Fruits: ", fruits, "\n\n")

# Accessing Items In A Tuple

print("The second fruit is: ", fruits[1])
print("The last fruit is: ", fruits[-1])
print("Fruits from second to fourth position: ", fruits[1:4])
print("Fruits from start to fourth position: ", fruits[:4])
print("Fruits from fourth position till the end: ", fruits[4:])
print("Fruits from fourth last to second last position: ", fruits[-4:-1],"\n\n")

# Getting the length of a Tuple

no_of_fruits = len(fruits)
print("Number of fruits: ", no_of_fruits, "\n\n")

# Combining two Tuple

vegetables = ("Spinach", "Onion", "Cucumber")
print("Vegetables: ",vegetables)
all_food = fruits + vegetables
print("Combined food: ", all_food, "\n\n")

# Deleting a Tuple

del vegetables

