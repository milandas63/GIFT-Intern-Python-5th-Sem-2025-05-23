class A:
    def funcA(self):
        print("This is class A")
class B(A):
    def funcA(self):
        print("This is class B")
class C(B):
    def funcA(self):
        print("This is class C")
class D(C, B):
    def funcA(self):
        print("This is class D")

obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()
obj1.funcA()
obj2.funcA()
obj3.funcA()
obj4.funcA()