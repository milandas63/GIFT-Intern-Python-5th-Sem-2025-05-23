def ascii_sum(s):
    sum=0
    for i in s:
        sum = sum + ord(i)
    return sum
stg= input("Enter your text:")
result=ascii_sum(stg)
print(f"The ascii sum of the text is:{result}")
