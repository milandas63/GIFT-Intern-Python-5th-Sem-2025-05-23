"""
("GIFT University", 45, "L", "-")
                              
------------------------------GIFT University......
 ---------------GIFT University--------------......
GIFT University------------------------------......
"""

def stretch(value, width, whichSide, padWith):
    value = str(value)
    if len(value)>=width:
        return value
    
    for i in range(len(value),width):
        if whichSide=='L':
            value = padWith+value
        elif whichSide=='C':
            if i%2==0:
                value = padWith+value
            else:
                value = value+padWith
        elif whichSide=='R':
                value = value+padWith

    return value

def justifyLeft(value, width, padWith):
    return stretch(value, width, "L", padWith)

def padL(value, width, padWith):
    return stretch(value, width, "L", padWith)

def justifyCenter(value, width, padWith):
    return stretch(value, width, "C", padWith)

def padC(value, width, padWith):
    return stretch(value, width, "C", padWith)

def justifyRight(value, width, padWith):
    return stretch(value, width, "R", padWith)

def padR(value, width, padWith):
    return stretch(value, width, "R", padWith)

