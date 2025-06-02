n = [[1,2,3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18]]
for i in range(len(n)-1, -1, -1):
    print(n[i])
    for j in n[i]:
        print(j)
