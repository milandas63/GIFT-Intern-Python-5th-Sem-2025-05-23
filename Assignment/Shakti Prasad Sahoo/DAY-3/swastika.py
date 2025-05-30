n = 9

for i in range(n):
    for j in range(n):

        if i < n // 2:
            if j == n - 1:
                    print("*", end="")
            elif j == n // 2:
                    print(" *", end="")
            elif i == 0 and j < n // 2:
                    print(" *", end="")
            else:
                    print("  ", end="")

        elif i == n // 2:
                print("* ", end="")

        else:
            if j == n // 2 or j == 0:
                    print("* ", end="")
            elif i == n - 1 and j > n // 2:
                    print("* ", end="")
            else:
                 print("  ", end="")
    print()