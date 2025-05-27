spaces = 40
for i in range(1,12):
    for j in range(0,spaces):
        print(" ",end="")
    for j in range(97,97+i):
        print(chr(j),end="")
    for j in range(97+i-2,96,-1):
        print(chr(j),end="")
    print()
    spaces = spaces-1

