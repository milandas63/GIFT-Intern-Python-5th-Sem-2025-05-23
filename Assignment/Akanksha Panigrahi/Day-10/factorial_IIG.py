def fact(num):
    if num<0:
        print("Factorial is not allowed for negative numbers.")
        return
    if num==0:
        return 1
    else:
        return num * fact(num-1)
    
number= int(input("Enter a number:"))
print (f"Factorial of {number} is:",fact(number))

    
    