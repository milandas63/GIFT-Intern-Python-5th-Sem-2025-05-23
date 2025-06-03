def rev_string(num):
    l=num.split()
    for i in range(len(l)-1,-1,-1):
        print(l[i],end = "")
        print(end= " ")
rev_string("America is an advanced country")