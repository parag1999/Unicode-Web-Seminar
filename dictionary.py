# Create  a dictionary:

empty_dict = {}
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car,"\n")

# Accessing Item

print("Car brand is: ", car["brand"], "\n")
print("Car year is : ", car.get("year"), "\n")

# Change Values

car["year"] = 2019
print("New Car year is : ", car["year"], "\n")

# Adding Values

car["colour"] = "Red"
print("After Adding colour: ", car, "\n")

# Removing Items

car.pop("colour")
print("After Removing colour: ", car, "\n")

# Copying a dictionary

car_copy = car.copy()
print("Copy of car: ", car_copy, "\n")

# Clearing a dictionary

car_copy.clear()
print("Emptied dictionary: ", car_copy, "\n\n")

# Deleting a dictionary

del car_copy
#print("Deleted dictionary: ", car_copy)

# Getting the length of a dictionary

no_of_car = len(car)
print("Number of car: ", no_of_car, "\n\n")

# Getting All the keys and Values

all_keys = car.keys()
all_values = car.values()
print(all_keys,all_values)



