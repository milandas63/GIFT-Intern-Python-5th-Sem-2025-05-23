#1.	Develop a class Calculator with methods to add and subtract two numbers.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
s= int(input("Enter first number: "))
v= int(input("Enter second number: "))
print("You have entered:", s, "and", v)
calculator = Calculator()
rsadd = calculator.add(s, v)
rssubtract = calculator.subtract(s, v)
print(f"first number:", s, "second number:", v, "Addition{s}+{v}:", rsadd)
print(f"first number:", s, "second number:", v, "Subtraction{s}-{v}:", rssubtract) 