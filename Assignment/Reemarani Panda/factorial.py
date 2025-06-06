def fact(n):
   if n<0:
      print("negative number are not edible")
   if n==0:
      return 1
   else:
      return n*fact(n-1)
n=int(input("enter a number to factorized:"))
print(f"factorial of (n) is={fact(n)}")

