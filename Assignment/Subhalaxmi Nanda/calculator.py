class calc:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1+self.n2
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def subtract(self):
        return self.n1-self.n2
o1=calc(9,8)
print(o1.add())
print(o1.subtract())
