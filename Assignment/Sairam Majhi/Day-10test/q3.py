spaces = 40
stars = 1
for i in range(1,10):
    for j in range(0,spaces):
        print(" ",end='')
    for j in range(0,stars):
        print("hellow",end='')
    print()
    spaces = spaces-5
    stars = stars+2