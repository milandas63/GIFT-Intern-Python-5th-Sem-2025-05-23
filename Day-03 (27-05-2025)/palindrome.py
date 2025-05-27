spaces = 40
for i in range(1,10):
    for j in range(0,spaces):
        print(" ",end="")
    for j in range(1,i):
        print(j,end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
    spaces = spaces-1

