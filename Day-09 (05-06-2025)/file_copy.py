print("COPY FILE TOOL")
source = input("Enter source file name: ")
target = input("Enter target file name: ")

handle1 = open(source, "r")
handle2 = open(target, "w")
content = handle1.read()
handle2.write(content)
handle2.close()
handle1.close()

print("Copy operation is successfully done")
