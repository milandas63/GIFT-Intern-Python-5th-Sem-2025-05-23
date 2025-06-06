num=int(input("Enter a number to get its factorial: "))
fr=1
while num>0:
    fr=fr*num
    num=num-1
print("The factorial of the given number is: ",fr)