text = input("enter the text :")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1


    else:
            frequency[char] = 1

print(frequency)