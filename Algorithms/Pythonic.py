key1 = input("Enter first word: ")
key2 = input("Enter second word: ")
if sorted(key1) == sorted(key2):
    print("Anagrams")
else:
    print(" not Anagrams")
