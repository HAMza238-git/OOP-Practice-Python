string = input("enter string")
vowels = 0
for i in string:
    if i in "aeiouAEIOU": 
       vowels = vowels+1
print(vowels)