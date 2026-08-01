text = input("enter")
frequency = {}

for char in text:
    if char in frequency :
        frequency[char] = frequency[char] + 1

    else:
        frequency[char] = 1

for char in text:
    if frequency[char] == 1:
        print(char)
        break




