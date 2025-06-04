
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
      
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

p = Puppy()
p.speak()  
p.bark()   
p.weep()   
