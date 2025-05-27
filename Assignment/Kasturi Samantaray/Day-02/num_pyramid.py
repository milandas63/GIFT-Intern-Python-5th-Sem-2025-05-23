spaces = 40
for i in range(1, 11):
    for j in range(0, spaces):
        print(" ", end = '')
    for j in range(1,i):
        print(i-1, end = '')
    for j in range(i, 0, -1):
        print(i-1, end = '')
    print(" ")
    spaces -= 1
    
