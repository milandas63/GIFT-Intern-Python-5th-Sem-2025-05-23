text = input("Enter a text: ")
vowels = "AEIOUaeiou"

count = 0
for i in text:
    for j in vowels:
        if i==j:
            count += 1

print("Vowels:",count)
