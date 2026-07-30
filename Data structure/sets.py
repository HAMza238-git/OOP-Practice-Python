fruits = set()

fruits.add("Apple")
fruits.add("Banana")
fruits.add("Orange")
fruits.add("Apple")      
fruits.add("Banana")    

print("Fruits:", fruits)

if "Apple" in fruits:
    print("Apple is available")

fruits.remove("Banana")
print("After removing Banana:", fruits)

fruits.add("Mango")
print("After adding Mango:", fruits)

print("Total Fruits:", len(fruits))

print("All Fruits:")
for fruit in fruits:
    print(fruit)

fruits.clear()
print("\nAfter clearing:", fruits)