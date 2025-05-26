for i in range(100,111,2):
    print(i)
    print("Python program")

spaces = 40
stars = 1
for i in range(1,11):
    for j in range(0,spaces):
        print(" ", end='')
    for j in range(0,stars):
        print("*", end='')
    print()
    spaces = spaces-1
    stars = stars+2


print(spaces, stars, "hello",sep=',')

