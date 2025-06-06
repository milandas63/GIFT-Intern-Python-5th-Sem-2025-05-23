#3.	Print a Hollow Inverted Pyramid Pattern.
def hollowinvpyramid(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()
n = 9
hollowinvpyramid(n)