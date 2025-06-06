def ascii(s):
    sum=0
    for i in s:
        sum=sum+ord(i) 
    return sum
print(ascii("Reema"))