numbers = [2, 5, 3, 2, 7, 3, 2]
target = 2
count = 0
for num in numbers:
    if num == target:
        count += 1

print(f"The target {target} appears {count} times in the list.")