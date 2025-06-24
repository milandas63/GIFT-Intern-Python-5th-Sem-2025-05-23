def equi_num(num):
    l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = ""
    for i in str(num):
        for j in l1:
            if int(i) == j:
                result = result + l2[l1.index(j)] + " "
    return result
print(equi_num(12345))





