text = input("input a string :")
count = 0
for i in text:
    if i.isalpha() and i not in "aeiouAEIOU":
        count += 1
print("the constant in string is ", count)
