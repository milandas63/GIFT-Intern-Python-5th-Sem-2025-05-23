#count the number of occurances of each character in a  given string
def countchar(s):
    charc = {}
    for char in s:
        if char in charc:
            charc[char] += 1
        else:
            charc[char] = 1
    return charc
s = input("Enter a string: ")
print(s)
result = countchar(s)
for char, count in result.items():
    if char != ' ': 
     print(f"{char} = {count}")