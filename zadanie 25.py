# Define a class, which have a class parameter and have a same instance parameter.

class Puppy:
    def __init__(self, name = "idk", race = "idk", age = 0):
        self.name = name
        self.race = race
        self.age = age
    def bark(self):
        print("My name is: " + self.name + "\n" + "I'm {} years old {}.".format(self.age, self.race))


p1 = Puppy("Reksio", "Kundel", 5)
p1.bark()