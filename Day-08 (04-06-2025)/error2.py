class AgeError(Exception):
    def __init__(self):
        print("Age Error",end=" ")

class InvalidAgeError(AgeError):
    def __init__(self):
        print("Invalid Age Error",end=" ")

class NegativeAgeError(InvalidAgeError):
    def __init__(self):
        print("Negative Age Error",end=" ")

class ZeroAgeError(InvalidAgeError):
    def __init__(self):
        print("Zero Age Error",end=" ")

class AgeCeilingError(AgeError):
    def __init__(self):
        print("Age Ceiling Error",end=" ")

class LowerAgeError(AgeCeilingError):
    def __init__(self):
        print("Lower Age Error",end=" ")

class UpperAgeError(AgeCeilingError):
    def __init__(self):
        print("Upper Age Error",end=" ")

ages = [27, 63, -33, 45, 66, 101, 54, 71, 0, 72, 81, -21, 16, 90, 55, 77]

for age in ages:
    try:
        if age<0:
            raise NegativeAgeError()
        elif age==0:
            raise ZeroAgeError()
        elif age<18:
            raise LowerAgeError()
        elif age>90:
            raise UpperAgeError()
        
        print(age,"is valid")
    except NegativeAgeError:
        print("Negative Age",age)
    except ZeroAgeError:
        print("Zero Age",age)
    except LowerAgeError:
        print("Lower Age",age)
    except UpperAgeError:
        print("Upper Age",age)
