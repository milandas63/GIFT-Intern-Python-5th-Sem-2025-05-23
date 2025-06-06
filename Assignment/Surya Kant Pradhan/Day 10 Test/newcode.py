
# Develop a class Calculator with methods to add and subtract two numbers.
x = int(input("enter a number"))
y = int(input("enter a another number"))
class Calculator:
    def add(self, x, y):
       
        return x + y

    def subtract(self, x, y):
       
        return x - y
calc = Calculator()
print(calc.add(x, y))
print(calc.subtract(x, y))

#Take a number from user and find the factorial of that number.

num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of",num,"is",fact)
