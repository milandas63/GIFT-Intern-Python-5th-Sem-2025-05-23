def reverse_word(s):
    l = s.split()
    for i in range(len(l)-1, -1, -1):
        print(l[i], end = " ")
reverse_word('America is an advanced country')