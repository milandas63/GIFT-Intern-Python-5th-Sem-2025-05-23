r = int(input("Enter number of rows: "))

for i in range(r, 0, -1):
    for s in range(r- i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i==r :
            print("*", end="")
        else:
            print(" ", end="")
    print()
