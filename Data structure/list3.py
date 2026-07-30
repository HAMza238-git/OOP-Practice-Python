number = [5, 2, 2, 4, 7, 8]
# sorting
number.sort()
print(number)
# sorting in decending
number.sort(reverse = True)
print(number)
# founding 7
if 7 in number:
    print("number found")

# printing max and min
print(max(number))
print(min(number))
# deleting 4 index
number.pop(4)
print(number)
# sum of number
print(sum(number))
# lenght of number
print(len(number))
# counting 2
print(number.count(2))
# reverse number
number.reverse()
print(number)
# removing duplicates
number = list(set(number))
print(number)
# average
age = [23, 56, 43]
average = sum(age) / len(age)
print(average)
# merge
merge = number + age
print(merge)
