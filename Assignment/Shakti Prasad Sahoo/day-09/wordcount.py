# write a program to count the number of words in a text file
fname = open("py.txt", "r")
def countword(file):
    text = file.read()
    words = text.split()
    return len(words)
content = fname.read()
print(content)
fname.seek(0)  
print(countword(fname))