n = 9
for i in range(1, n + 1):
    num_list = list(range(i, 0, -1)) + list(range(2, i + 1))
    print(' ' * (n - i) + ''.join(str(num) for num in num_list))