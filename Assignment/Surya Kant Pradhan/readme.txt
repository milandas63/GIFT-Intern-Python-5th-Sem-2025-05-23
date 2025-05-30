
def count_characters(text):
    
    text = text.upper()

   
    text = text.replace(" ", "")

   
    char_count = {}

    
    for char in text:
        if char in char_count:
        
            char_count[char] += 1
        else:
           
            char_count[char] = 1

    
    for char in sorted(char_count):
        print(char, "-", char_count[char])


print("Hello World")
count_characters("Hello World")

print("\nStudents Allowed")
count_characters("Students Allowed")

print("\nHolocaust")
count_characters("Holocaust")




Output:

Hello World
D - 1
E - 1
H - 1
L - 3
O - 2
R - 1
W - 1

Students Allowed
A - 1
D - 2
E - 2
L - 2
N - 1
O - 1
S - 2
T - 2
U - 1
W - 1

Holocaust
A - 1
C - 1
H - 1
L - 1
O - 2
S - 1
T - 1
U - 1



