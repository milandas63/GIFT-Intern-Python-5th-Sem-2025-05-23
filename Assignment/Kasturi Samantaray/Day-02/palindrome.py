spaces = 40
str = 'abcdefghij'
for i in range(1, 11):
    for j in range(0, spaces):
        print(" ", end = '')
    for j in range(1, i):
        print(str[j-1], end = '')
    for j in range(i,0, -1):
        print(str[j-1], end = '')
    print(" ")
    spaces -= 1
