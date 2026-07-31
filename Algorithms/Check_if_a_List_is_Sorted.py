numbers = [7, 2, 5, 7, 9, 12]
is_sorted = True

for i in range (len(numbers) - 1):
    if numbers[i] > numbers[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("sorted")
else:
    print("not sorted")


