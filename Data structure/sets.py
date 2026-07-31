fruits = set()

fruits.add("apple")
fruits.add("banana")
fruits.add("orange")

print(fruits)

if "apple" in fruits:
    print("apple is in fruit")

fruits.remove("orange")
print(fruits)

fruits.add("mango")
print(fruits)

print("lenght of fruits", len(fruits))

for fruit in fruits:
    print(fruit)

fruits.clear()
print(fruits)