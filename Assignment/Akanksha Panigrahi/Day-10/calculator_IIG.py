class Calc:
    def __init__(self,num1,num2):
        self.num1,self.num2= num1,num2
    def add (self):
        return self.num1+self.num2
    def sub (self):
        return self.num1-self.num2
obj1= Calc(10,20)
print("For Addition:")
print(obj1.add())
print ("For Subtraction:")
print(obj1.sub())