x = "Bird"

def run():
    global x
    x = "Fish"
    print("Within run() function: ",x)


run()

print("Outside run() function: ",x)

