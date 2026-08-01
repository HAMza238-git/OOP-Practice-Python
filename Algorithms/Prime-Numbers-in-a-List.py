numbers = [2, 5, 8, 11, 15, 17, 20]
new = []

for num in numbers:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    if is_prime:
        new.append(num)
        

print(new)



    