text = input("Enter a text: ")

sum = []
for i in range(0,26):
    sum.append(0)

asc = 0
for i in text:
    asc = ord(i)
    if asc>=65 and asc<=90:    # capital alphabets
        asc -= 65
        sum[asc] = sum[asc]+1
    elif asc>=97 and asc<=122: # small alphabets
        asc -= 97
        sum[asc] = sum[asc]+1

for i in range(0,26):
    if sum[i]>0:
        print(chr(i+65),"=",sum[i])
