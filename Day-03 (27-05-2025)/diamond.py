spaces = 40
stars = 1
for i in range(1,22):
    for j in range(0,spaces):
        print(" ",end="")
    for j in range(0,stars):
        print("*",end="")
    print()
    if(i<10):
        spaces = spaces-1
        stars = stars+2
    else:
        spaces = spaces+1
        stars = stars-2
