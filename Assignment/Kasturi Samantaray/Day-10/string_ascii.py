def ascii_sum(s):
    sum = 0
    for i in s:
        sum = sum + ord(i)
    return sum
text = input("Enter a string : ")
result = ascii_sum(text)
print(f"The ASCII sum of the characters in the string is : {result}")
