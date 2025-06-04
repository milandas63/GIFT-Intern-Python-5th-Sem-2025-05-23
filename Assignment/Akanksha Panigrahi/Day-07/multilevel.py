# class a:
#     def A(self):
#         print("Class A")
# class b(a):
#     def B(self):
#         print("Class B")
# class c(b):
#     def C(self):
#         print("Class C")


class a:
    def A(self):
        print("Class A")
class b(a):
    def B(self):
        print("Class B")
class c(b,a):
    def C(self):
        print("Class C")
obj1=a()
obj2=b()
obj3=c()
obj1.A()
obj2.B()
obj3.C()
