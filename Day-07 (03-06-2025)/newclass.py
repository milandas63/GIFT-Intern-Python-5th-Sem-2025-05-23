class a():
    def __init__(self):
        print("Printing from a")

    def funcA(self):
        print("Function in A")

class b(a):
    def __init__(self):
        print("Printing from b")

o1 = b()
o1.funcA()

