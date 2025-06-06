def fact(n):
    if n<0:
        print("negetive numbers are not allowed!")
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a number to be factorized:"))
print(f"factorial of {n} is = {fact(n)}")