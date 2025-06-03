def reverse_words(s):
    l = s.split()
    for i in l:
        for j in range(len(i)-1, -1, -1):
            print(list(i)[j], end = '')
        print(end = " ")
reverse_words('America is an advanced country')
