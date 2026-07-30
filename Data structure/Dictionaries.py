fruits = {}
fruits["apple"] = 120
fruits["banana"] = 90
fruits["orange"] = 140

print(fruits)

fruits["banana"] = 100
print (fruits)

fruits["mango"] = 200
print(fruits)

del fruits["orange"]
print(fruits)

print("fruits", len(fruits))
print(fruits)

for fruit, price in fruits.items():
    print(fruit, ":", price)

fruits.clear()
print(fruits)