text = input("Enter some text using upper & lower case: ")
print(text)
for i in text:
    ascii = ord(i)
    if(ascii>=65 and ascii<=90):   # upper-case
        ascii += 32
    elif(ascii>=97 and ascii<=122):
        ascii -= 32
    k = chr(ascii)
    print(k,end='')

