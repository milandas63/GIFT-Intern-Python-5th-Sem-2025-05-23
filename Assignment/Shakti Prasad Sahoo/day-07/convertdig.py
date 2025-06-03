# Convert all digits in a number to their respective words
digitword = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

number = input("Enter a number: ")
print("You entered:", number)
result = []

for digit in number:
    if digit.isdigit():
        result.append(digitword[int(digit)])
    else:
        result.append(digit) 

print(' '.join(result))