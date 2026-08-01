string = input("enter a string : ")
current_word = ""
longest_word = ""
for char in string:
    if char != " ":
        current_word = current_word + char
    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""

    if len(current_word) > len(longest_word):
        longest_word = current_word
# longest_word = max(string.split(), key=len)


print(longest_word)

