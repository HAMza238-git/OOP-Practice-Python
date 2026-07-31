number = [3,5,7,8,3]
reverse_number = []

lenght = len(number) - 1

while lenght >= 0:
    reverse_number.append(number[lenght])
    lenght -= 1

print(reverse_number)

