numbers = [4, 7, 10, 15, 18, 21, 30]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even is", even_count)
print("odd is", odd_count)