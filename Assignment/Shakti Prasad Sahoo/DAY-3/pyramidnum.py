rows = 10  

for i in range(rows):
    digit = str(i % 10)  
    spaces = ' ' * (rows - i - 1)
    digits = digit * (2 * i + 1)
    print(spaces + digits)
