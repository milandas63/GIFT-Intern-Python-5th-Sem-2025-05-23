# count the number of  words in a given string
text = input("Enter a string: ")
print("text entered:", text)
words = text.split()
word_count = len(words)
print(f"The number of words in the string is: {word_count}")

# reverse the order of words in a given string
reversedtext = ' '.join(reversed(words))
print("Reversed text:", reversedtext)

# reverse the content of  each wordin a given string
reversedwords = [word[::-1] for word in words]
print("Reversed words:", ' '.join(reversedwords))