string = input("enter a string : ")
final = ""

for char in string:
    if char not in final:
        final += char

print(final)