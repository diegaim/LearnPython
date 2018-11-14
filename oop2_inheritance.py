#Parent
class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

#Child
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Child
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Main
jim = Bulldog("Jim", 7)
print(jim.description())
print(jim.run(120))
print(isinstance(jim, Dog)) #Check is jim(type : Bulldog) is intance from dog class or not