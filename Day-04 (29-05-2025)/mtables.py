start = 2
end = 26
def padL(value, width):
    retval = str(value)
    for i in range(len(retval),width):
        retval = " "+retval
    return retval

for h in range(start,end+1,6):
    for i in range(1,11):
        for j in range(h,h+6):
            if j<=end:
                print(padL(j,2),"x",padL(i,2),"=",padL(j*i,3), end="  ")
        print()
    print()
