import foo

text = "An abstract class provides default implementations"
ltext = text.split()
l = 0
for i in ltext:
    if len(i)>l:
        l = len(i)
for j in range(0,l+4):
    print("*", end="")
print()
for i in ltext:
    print("* "+foo.padR(i,l," ")+" *")
for j in range(0,l+4):
    print("*", end="")
print()
