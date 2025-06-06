class calculator:
    def __init__(self, num1, num2):
        self.num1 , self.num2 = num1, num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2

obj1 = calculator(1, 2)
print("ADDITION :-")
print(obj1.add())
print("SUBTRACTION :-")
print(obj1.subtract())
