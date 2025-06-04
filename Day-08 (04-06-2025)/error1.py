class My(Exception):
    def __init__(self):
        print("My")

class MyError(Exception):
    def __init__(self):
        print("MyError")

try:
    raise My()
    x = 239
    y = 0
    print('X=',x)
    print('Y=',y)
    z = x / y
    print('Z=',z)
    print('Hello World')
except MyError:
    print("This is MyError")
except ZeroDivisionError:
    print("Zero Division")
except My:
    print("Error")

