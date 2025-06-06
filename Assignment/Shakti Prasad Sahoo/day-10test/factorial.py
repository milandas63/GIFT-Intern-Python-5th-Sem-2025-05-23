#4.	Take a number from user and find the factorial of that number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number: "))
if n < 0:
    print("Factorial not defined for negative numbers.")
else:
    print(f"The factorial of {n} is {factorial(n)}" ,end='')  