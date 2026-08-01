text = input("enter a string : ")
reverse = ""

for i in range(len(text) -1, -1, -1):
    text[i]
    reverse = reverse + text[i]

if reverse == text:
    print("palindrome")
else:
    print("not palindrome")



# reverse = text[::-1]
# if reverse == text:
#     print("palindrome")
# else:
#     print("not palindrome")


