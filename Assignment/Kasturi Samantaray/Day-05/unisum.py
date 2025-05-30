def unisum(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    if sum >= 10:
        sum = unisum(sum)
    return sum

text = int(input("Enter a number : "))
result = unisum(text)
print(f"The single digit sum of {text} is {result} !!")
print()
       