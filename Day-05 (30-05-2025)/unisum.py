num = input("Enter a number: ")
while(True):
    e = 0
    sum = 0
    for n in num:
        e = int(n)
        sum = sum + e
    
    num = str(sum)
    if(len(num)>1):
        print(num)
        continue
    else:
        print(num)
        break
