#5.	Take a string from user and Sum the ASCII values of the characters in that String.
def sumasciival(s):
    total = 0
    for char in s:
        total += ord(char)
    return total
s = input("Enter a string to get the sum of the ascii values: ")
print(f"The sum of the ASCII values in '{s}' is {sumasciival(s)}", end='')