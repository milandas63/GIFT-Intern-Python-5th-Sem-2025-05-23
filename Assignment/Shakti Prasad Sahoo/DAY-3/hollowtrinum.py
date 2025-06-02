n =9
for i in range(1, n + 1):
    if i == 1:
        print(' ' * (n - i) + '1')
    elif i == n:
        print(''.join(str(j) for j in range(n, 0, -1)) + ''.join(str(j) for j in range(2, n + 1)))
    else:
        print(' ' * (n - i) + str(i) + ' ' * (2 * i - 3) + str(i))