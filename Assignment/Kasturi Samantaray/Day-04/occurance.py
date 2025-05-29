def occurance(s):
    d = {i:0 for i in s}
    for i in s:
        if i in d.keys():
            d[i] += 1
    
    for keys, values in d.items():
        if keys == " ":
            continue
        print(f"{keys} : {values}")
occurance("Hello World")