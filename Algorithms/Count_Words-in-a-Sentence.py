string = input("enter a string : ")
count = 1

for char in string:
    if char == ' ':
        count += 1

print(count)