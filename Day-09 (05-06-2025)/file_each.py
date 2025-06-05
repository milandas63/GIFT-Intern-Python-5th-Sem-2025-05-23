handle = open("example_text.txt", "r")

for one in iter(lambda: handle.read(1), ""):
    print(one)

handle.close()
