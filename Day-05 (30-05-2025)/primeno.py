"""
Print all PRIME NUMBERS between 2 given numbers?
    Say: 1500 and 3000
"""

start = 1500
end = 3000

line = 0
for i in range(start, end+1):
    yes = True
    for j in range(2,int(i/2)):
        r = i%j
        if r==0:
            yes = False
            break
    if yes:
        print(i, end='  ')
        line += 1
        if line>15:
            line = 0
            print()

