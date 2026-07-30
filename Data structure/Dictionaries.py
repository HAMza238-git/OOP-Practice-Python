fruits = {}

fruits["Apple"] = 120
fruits["Banana"] = 80
fruits["Orange"] = 150

print("Fruits:", fruits)

print("Price of Apple:")
print(fruits["Apple"])

fruits["Banana"] = 90
print("After Updating Banana:")
print(fruits)

fruits["Mango"] = 200
print("After Adding Mango:")
print(fruits)

del fruits["Orange"]
print("After Removing Orange:")
print(fruits)

print("Total Fruits:", len(fruits))

print("Fruit Prices:")
for fruit, price in fruits.items():
    print(fruit, ":", price)

fruits.clear()
print("\nAfter Clearing:", fruits)